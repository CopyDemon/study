"""play ground for material project contribs api playground

Raises:
    Exception: _description_
"""

import logging
import json

from mpcontribs.client import Client
from mp_api.client import MPRester

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# app setups
# load api key

########################################################
# API CALLS
########################################################
class MPContribsClient:
    """MPContribsClient class to interact with mpcontribs-client
    
    Args:
        api_key (str): api key for mpcontribs-client
        
    Attributes:
        api_key (str): api key for mpcontribs-client
    """
    def __init__(self, api_key:str):
        self.api_key = api_key
        self.mpr = MPRester(api_key=self.api_key)
        self.client = Client(apikey=self.api_key, host='ml-api.materialsproject.org')
        
    def show_available_resources_for_mpr(self):
        """show available resources of mpcontribs-client
        """
        try:
            available_resources = dir(self.mpr)
            logger.info("available resources for mpr(MPRester) is: %s", json.dumps(available_resources, indent=4))
        except Exception as e:
            logger.error("Failed to show available resources: %s", e)
            raise e
        
    def show_available_resources_for_mpr_contribs(self):
        """show available resources of mpcontribs-client
        """
        try:
            available_resources = dir(self.client)
            logger.info("available resources for mpr(MPRester) contribs is: %s", json.dumps(available_resources, indent=4))
        except Exception as e:
            logger.error("Failed to show available resources: %s", e)
        
    def query_projects(self):
        """query projects from mpcontribs-client

        Returns:
            list: list of projects
        """
        projects = self.mpr.contribs.query_projects(fields=["name"])
        # logger.info("projects: %s", json.dumps(projects, indent=4))
        return projects
    
    def query_all_contribs_ids(self):
        """query all contribs ids from mpcontribs-client
        """
        contribs_ids = self.mpr.contribs.get_all_ids()
        logger.info("find %s contribs ids", len(contribs_ids))
        logger.info("contribs ids: %s", json.dumps(contribs_ids, indent=4))
        return contribs_ids

    def find_project_by_name(self, project_name: str):
        """通过项目名称查找项目信息
        
        Args:
            project_name (str): 项目名称，比如 "Carrier Transport"
            
        Returns:
            dict: 项目信息，包含 project_id 和其他详细信息
        """
        try:
            # 查询所有项目，包含更多字段
            projects = self.mpr.contribs.query_projects(fields=["name", "title", "description", "owner"])
            
            # 查找匹配的项目
            matching_projects = []
            for project in projects:
                if project_name.lower() in project.get("name", "").lower():
                    matching_projects.append(project)
                    
            if not matching_projects:
                logger.warning("未找到名为 '%s' 的项目", project_name)
                return None
                
            if len(matching_projects) > 1:
                logger.info("找到 %d 个包含 '%s' 的项目:", len(matching_projects), project_name)
                for i, project in enumerate(matching_projects):
                    logger.info("  %d. %s (ID: %s)", i+1, project.get("name"), project.get("project_id"))
                    
            return matching_projects[0]  # 返回第一个匹配的项目
            
        except Exception as e:
            logger.error("查找项目时出错: %s", e)
            raise e

    def query_contributions_by_project_name(self, project_name: str, limit: int = 100):
        """通过项目名称查询该项目的所有contributions
        
        Args:
            project_name (str): 项目名称，比如 "carrier_transport"
            limit (int): 返回结果的最大数量，默认100
            
        Returns:
            list: contributions列表
        """
        try:
            # 首先找到项目
            project = self.find_project_by_name(project_name)
            if not project:
                logger.error("未找到项目: %s", project_name)
                return []
                
            project_name_actual = project.get("name")
            logger.info("找到项目: %s", project_name_actual)
            
            # 使用正确的查询格式 - 查询字典中指定project
            query_dict = {
                "project": project_name_actual  # 在query字典中指定项目名
            }
            
            logger.info("查询字典: %s", query_dict)
            logger.info("限制数量: %d", limit)
            
            # 查询该项目的contributions - 使用正确的参数格式
            result = self.mpr.contribs.query_contributions(
                query=query_dict,
                fields=["id", "identifier", "formula", "project", "is_public", "last_modified"]
            )
            
            # 处理分页 - 如果需要更多数据
            all_contributions = []
            if isinstance(result, dict) and 'data' in result:
                contributions = result['data']
                all_contributions.extend(contributions)
                
                # 如果有更多数据且还没达到限制，继续获取
                total_count = result.get('total_count', len(contributions))
                has_more = result.get('has_more', False)
                
                logger.info("第一页获取到 %d 个contributions (总计: %d)", len(contributions), total_count)
                
                # 如果需要更多数据并且总数超过第一页
                page = 2
                while has_more and len(all_contributions) < limit and len(all_contributions) < total_count:
                    logger.info("获取第 %d 页数据...", page)
                    
                    # 使用分页获取更多数据
                    next_result = self.mpr.contribs.query_contributions(
                        query=query_dict,
                        fields=["id", "identifier", "formula", "project", "is_public", "last_modified"]
                        # MPRester 会自动处理分页
                    )
                    
                    if isinstance(next_result, dict) and 'data' in next_result:
                        more_contributions = next_result['data']
                        all_contributions.extend(more_contributions)
                        has_more = next_result.get('has_more', False)
                        page += 1
                    else:
                        break
                
                # 限制返回的数量
                final_contributions = all_contributions[:limit]
                
                logger.info("成功获取到项目 '%s' 的 %d 个contributions (请求限制: %d, 总计: %d)", 
                          project_name_actual, len(final_contributions), limit, total_count)
                
                # 显示前几个示例
                display_count = min(5, len(final_contributions))
                logger.info("显示前 %d 个contributions:", display_count)
                for i in range(display_count):
                    contrib = final_contributions[i]
                    logger.info("Contribution %d:", i+1)
                    logger.info("  - ID: %s", contrib.get("id", "N/A"))
                    logger.info("  - 标识符: %s", contrib.get("identifier", "N/A"))
                    logger.info("  - 公式: %s", contrib.get("formula", "N/A"))
                    logger.info("  - 项目: %s", contrib.get("project", "N/A"))
                    logger.info("  - 是否公开: %s", contrib.get("is_public", "N/A"))
                    logger.info("  - 最后修改: %s", contrib.get("last_modified", "N/A"))
                
                return final_contributions
            else:
                logger.error("API返回格式异常: %s", type(result))
                logger.error("返回内容: %s", result)
                return []
                
        except Exception as e:
            logger.error("查询contributions时出错: %s", e)
            import traceback
            logger.error("详细错误信息: %s", traceback.format_exc())
            return []

    def get_detailed_contribution_info(self, project_name: str, contribution_id: str):
        """获取特定contribution的详细信息
        
        Args:
            project_name (str): 项目名称
            contribution_id (str): contribution的ID
            
        Returns:
            dict: contribution的详细信息
        """
        try:
            logger.info("获取contribution详细信息...")
            logger.info("  项目: %s", project_name)
            logger.info("  Contribution ID: %s", contribution_id)
            
            # 直接使用contribution_id获取详细信息，不需要project_id
            contribution = self.mpr.contribs.get_contribution(contribution_id)
            
            logger.info("✅ 成功获取contribution详细信息")
            logger.info("Contribution详细信息:")
            logger.info("  📋 基本信息:")
            logger.info("    - 项目: %s", contribution.get("project", "N/A"))
            logger.info("    - 标识符: %s", contribution.get("identifier", "N/A"))
            logger.info("    - 公式: %s", contribution.get("formula", "N/A"))
            logger.info("    - 是否公开: %s", contribution.get("is_public", "N/A"))
            logger.info("    - 最后修改: %s", contribution.get("last_modified", "N/A"))
            
            # 显示所有可用的键
            all_keys = list(contribution.keys())
            logger.info("  🗂️  所有可用数据字段 (%d个):", len(all_keys))
            for i, key in enumerate(all_keys[:20]):  # 显示前20个键
                logger.info("    %d. %s", i+1, key)
            if len(all_keys) > 20:
                logger.info("    ... 还有 %d 个字段", len(all_keys) - 20)
            
            # 如果有data字段，显示其结构
            if 'data' in contribution:
                data = contribution['data']
                if isinstance(data, dict):
                    data_keys = list(data.keys())
                    logger.info("  📊 数据内容字段 (%d个):", len(data_keys))
                    for i, key in enumerate(data_keys[:10]):  # 显示前10个数据字段
                        value = data.get(key)
                        if isinstance(value, (int, float, str, bool)):
                            logger.info("    %d. %s: %s", i+1, key, str(value)[:50])
                        else:
                            logger.info("    %d. %s: <%s>", i+1, key, type(value).__name__)
                    if len(data_keys) > 10:
                        logger.info("    ... 还有 %d 个数据字段", len(data_keys) - 10)
            
            return contribution
            
        except Exception as e:
            logger.error("获取contribution详细信息时出错: %s", e)
            import traceback
            logger.error("详细错误信息: %s", traceback.format_exc())
            return None

    def list_all_project_names(self, limit: int = None):
        """列出所有项目名称
        
        Args:
            limit (int): 显示项目数量限制，None表示显示所有
            
        Returns:
            list: 项目名称列表
        """
        try:
            # 查询所有项目
            projects = self.mpr.contribs.query_projects(fields=["name", "title", "description"])
            
            project_names = []
            logger.info("所有可用的项目 (共 %d 个):", len(projects))
            
            display_count = limit if limit else len(projects)
            for i, project in enumerate(projects[:display_count]):
                name = project.get("name", "N/A")
                title = project.get("title", "")
                project_names.append(name)
                
                # 显示项目信息
                display_title = f" - {title}" if title and title != name else ""
                logger.info("  %d. %s%s", i+1, name, display_title)
                
            if limit and len(projects) > limit:
                logger.info("  ... 还有 %d 个项目 (使用 limit=None 查看所有)", len(projects) - limit)
                
            return project_names
            
        except Exception as e:
            logger.error("获取项目列表时出错: %s", e)
            raise e

    def inspect_query_contributions_method(self):
        """检查query_contributions方法的参数和签名
        """
        try:
            import inspect
            
            # 获取方法签名
            method = self.mpr.contribs.query_contributions
            signature = inspect.signature(method)
            
            logger.info("query_contributions方法签名:")
            logger.info("  %s", signature)
            
            # 获取参数信息
            logger.info("参数详情:")
            for param_name, param in signature.parameters.items():
                default = param.default if param.default != param.empty else "无默认值"
                logger.info("  - %s: %s (默认值: %s)", param_name, param.annotation, default)
                
            # 尝试获取方法文档
            if method.__doc__:
                logger.info("方法文档:")
                logger.info("  %s", method.__doc__)
                
        except Exception as e:
            logger.error("检查方法签名时出错: %s", e)
            
    def get_sample_contributions(self, count: int = 5):
        """获取一些示例contributions来了解数据结构
        
        Args:
            count (int): 获取的示例数量
            
        Returns:
            list: contributions列表
        """
        try:
            logger.info("获取 %d 个示例contributions...", count)
            
            # 尝试最简单的查询
            result = self.mpr.contribs.query_contributions()
            
            logger.info("查询结果类型: %s", type(result))
            logger.info("查询结果键: %s", list(result.keys()) if isinstance(result, dict) else "不是字典")
            
            # 如果结果是字典，尝试获取data或类似的键
            if isinstance(result, dict):
                # 常见的可能键名
                possible_keys = ['data', 'results', 'contributions', 'items']
                contributions_data = None
                
                for key in possible_keys:
                    if key in result:
                        contributions_data = result[key]
                        logger.info("找到contributions数据在键 '%s', 数量: %d", key, len(contributions_data))
                        break
                        
                if contributions_data is None:
                    # 如果没有找到标准键，显示所有键的内容
                    logger.info("未找到标准数据键，显示所有键的内容:")
                    for key, value in result.items():
                        logger.info("  键 '%s': %s (类型: %s)", key, str(value)[:100], type(value))
                    return []
                    
            else:
                contributions_data = result
                
            # 显示前几个示例
            display_count = min(count, len(contributions_data))
            for i in range(display_count):
                contrib = contributions_data[i]
                logger.info("示例 %d:", i+1)
                logger.info("  - 标识符: %s", contrib.get("identifier", "N/A"))
                logger.info("  - 公式: %s", contrib.get("formula", "N/A"))
                logger.info("  - 项目: %s", contrib.get("project", "N/A"))
                logger.info("  - 所有键: %s", list(contrib.keys()))
                
            return contributions_data[:count]
            
        except Exception as e:
            logger.error("获取示例contributions时出错: %s", e)
            raise e

    def check_available_query_params(self):
        """检查可用的查询参数
        """
        try:
            logger.info("检查可用的查询参数...")
            available_params = self.mpr.contribs.available_query_params()
            
            logger.info("可用的查询参数:")
            if isinstance(available_params, dict):
                for param, info in available_params.items():
                    logger.info("  - %s: %s", param, info)
            else:
                logger.info("  %s", available_params)
                
            return available_params
            
        except Exception as e:
            logger.error("检查查询参数时出错: %s", e)
            raise e

    def query_project_contributions_summary(self, project_name: str, sample_size: int = 5):
        """获取指定项目的contributions概况信息
        
        Args:
            project_name (str): 项目名称，比如 "carrier_transport"
            sample_size (int): 显示的示例数量，默认5个
            
        Returns:
            dict: 包含项目概况信息的字典
        """
        try:
            logger.info("🔍 查询项目 '%s' 的contributions概况...", project_name)
            
            # 1. 首先验证项目是否存在
            project = self.find_project_by_name(project_name)
            if not project:
                logger.error("❌ 未找到项目: %s", project_name)
                return None
                
            project_title = project.get("title", "N/A")
            logger.info("✅ 找到项目: %s - %s", project_name, project_title)
            
            # 2. 查询该项目的contributions总数
            query_dict = {"project": project_name}
            result = self.mpr.contribs.query_contributions(query=query_dict)
            
            total_count = result.get('total_count', 0)
            contributions = result.get('data', [])
            
            logger.info("📊 项目概况:")
            logger.info("   - 项目名称: %s", project_name)
            logger.info("   - 项目标题: %s", project_title)
            logger.info("   - 总contributions数: %s", total_count)
            
            # 3. 显示前几个示例contributions
            if contributions and sample_size > 0:
                logger.info("📋 示例contributions (前 %d 个):", min(sample_size, len(contributions)))
                
                for i, contrib in enumerate(contributions[:sample_size]):
                    contrib_id = contrib.get('id', 'N/A')
                    identifier = contrib.get('identifier', 'N/A')
                    formula = contrib.get('formula', 'N/A')
                    is_public = contrib.get('is_public', False)
                    last_modified = contrib.get('last_modified', 'N/A')
                    
                    logger.info("   %d. %s (%s)", i+1, identifier, formula)
                    logger.info("      - 内部ID: %s", contrib_id)
                    logger.info("      - 公开状态: %s", "公开" if is_public else "私有")
                    logger.info("      - 最后修改: %s", last_modified)
            
            # 4. 返回概况信息
            summary = {
                "project_name": project_name,
                "project_title": project_title,
                "total_contributions": total_count,
                "sample_contributions": contributions[:sample_size] if contributions else [],
                "success": True
            }
            
            logger.info("✅ 项目概况查询完成")
            return summary
            
        except Exception as e:
            logger.error("❌ 查询项目contributions概况时出错: %s", e)
            import traceback
            logger.error("详细错误信息: %s", traceback.format_exc())
            return {
                "project_name": project_name,
                "success": False,
                "error": str(e)
            }

    def quick_project_query(self, project_name: str, num_examples: int = 5):
        """便捷方法：快速查询指定项目的contributions信息
        
        这是一个简化的方法，用于快速获取项目的基本信息和示例数据。
        
        Args:
            project_name (str): 项目名称，例如：
                - "carrier_transport" (Carrier Transport项目)
                - "2dmatpedia" (2DMatPedia项目)
                - "defect_genome_pcfc_materials" (Defect Genome PCFC项目)
            num_examples (int): 显示的示例contributions数量，默认5个
            
        Returns:
            dict: 包含项目信息和示例数据的字典
            
        Example:
            >>> client = MPContribsClient(api_key)
            >>> result = client.quick_project_query("carrier_transport")
            >>> print(f"项目有 {result['total_count']} 个contributions")
        """
        try:
            print(f"🔍 正在查询项目: {project_name}")
            
            # 首先找到项目基本信息
            project = self.find_project_by_name(project_name)
            if not project:
                return {"success": False, "error": f"项目未找到: {project_name}"}
            
            project_title = project.get("title", "N/A")
            print(f"✅ 找到项目: {project_name} - {project_title}")
            
            # 2. 查询该项目的contributions
            contributions = self.query_contributions_by_project_name(project_name, limit=200)
            
            if not contributions:
                print("❌ 该项目没有contributions数据")
                return {"success": False, "error": "No contributions found"}
            
            # 获取总数信息 - 从query_contributions_by_project_name的返回结果中获取
            total_count = len(contributions) if isinstance(contributions, list) else 0
            
            # 3. 获取前几个contributions的详细信息
            sample_contributions = contributions[:num_examples] if len(contributions) > num_examples else contributions
            
            print(f"✅ 项目查询成功!")
            print(f"   📊 统计信息:")
            print(f"      - 项目标题: {project_title}")
            print(f"      - 获取到的contributions数: {total_count:,}")
            print(f"      - 示例数量: {len(sample_contributions)}")
            
            print(f"\n   🔍 示例contributions:")
            for i, contrib in enumerate(sample_contributions, 1):
                identifier = contrib.get('identifier', 'N/A')
                formula = contrib.get('formula', 'N/A')
                is_public = contrib.get('is_public', False)
                print(f"      {i}. {identifier} - {formula} ({'公开' if is_public else '私有'})")
            
            return {
                "success": True,
                "project_name": project_name,
                "project_title": project_title,
                "total_count": total_count,
                "sample_count": len(sample_contributions),
                "sample_contributions": sample_contributions
            }
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"查询项目时出错: {error_msg}")
            return {
                "success": False,
                "error": error_msg,
                "project_name": project_name
            }





