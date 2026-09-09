# 通过项目名称查询Material Project Contributions完整教程

## 📋 目录
1. [概述](#概述)
2. [技术原理](#技术原理)
3. [详细步骤](#详细步骤)
4. [代码实现](#代码实现)
5. [实际演示](#实际演示)
6. [常见问题](#常见问题)
7. [进阶技巧](#进阶技巧)

---

## 概述

本教程将一步一步教会你如何通过项目名称（如"Carrier Transport"）来查询该项目下的所有contributions数据。

### 🎯 学习目标
- 理解Material Project Contributions的数据结构
- 掌握从项目名称到contributions的完整查询流程
- 学会使用API进行精确查询
- 能够处理查询结果和错误情况

### 📦 所需工具
- `mp-api` 包：`from mp_api.client import MPRester`
- API密钥：Material Project的有效API key
- Python 3.7+

---

## 技术原理

### 🔍 查询流程概述
```
项目名称 → 验证项目存在 → 获取项目详情 → 查询contributions → 处理结果
   ↓              ↓              ↓              ↓              ↓
"carrier_     项目列表中     project对象    contributions   结构化数据
transport"    查找匹配      包含元数据        列表          和统计信息
```

### 📚 核心概念

1. **项目(Project)**: 包含特定类型数据的集合，如"载流子传输"、"二维材料"等
2. **Contribution**: 项目中的单个数据条目，通常对应一个材料的计算结果
3. **查询参数**: 用于筛选和限制查询结果的条件

---

## 详细步骤

### 第1步：初始化API客户端

```python
from mp_api.client import MPRester

# 使用API密钥创建客户端
api_key = "你的API密钥"
mpr = MPRester(api_key=api_key)
```

**重要说明**：
- 使用 `MPRester` 而不是 `mpcontribs.client.Client`
- `MPRester` 通过Material Project统一API访问，能获取完整数据
- `mpcontribs.client.Client` 直接连接MPContribs，有默认过滤条件

### 第2步：查询所有可用项目

```python
# 获取所有项目列表
projects = mpr.contribs.query_projects(fields=["name", "title", "description"])

print(f"总共有 {len(projects)} 个项目")
for project in projects[:5]:  # 显示前5个
    print(f"- {project.get('name')} : {project.get('title')}")
```

**技术细节**：
- `query_projects()` 返回所有可用项目的列表
- `fields` 参数指定返回的字段，减少不必要的数据传输
- 项目名称(`name`)是API查询的关键标识符

### 第3步：根据名称查找特定项目

```python
def find_project_by_name(project_name):
    """根据项目名称查找项目"""
    projects = mpr.contribs.query_projects(fields=["name", "title", "description"])
    
    for project in projects:
        if project.get("name") == project_name:
            return project
    return None

# 查找Carrier Transport项目
project = find_project_by_name("carrier_transport")
if project:
    print(f"找到项目: {project.get('name')} - {project.get('title')}")
else:
    print("项目未找到")
```

**关键点**：
- 项目名称必须精确匹配（大小写敏感）
- 实际名称可能与显示标题不同（如"Carrier Transport" 项目名是 "carrier_transport"）
- 建议先列出所有项目名称，确认正确的名称格式

### 第4步：查询项目的Contributions

```python
def query_contributions_by_project(project_name, limit=100):
    """查询指定项目的contributions"""
    
    # 构建查询参数
    query_params = {
        "project": project_name  # 关键：使用project参数筛选
    }
    
    # 执行查询
    result = mpr.contribs.query_contributions(
        query=query_params,  # 传入查询字典
        limit=limit,         # 限制返回数量
        fields=["identifier", "formula", "project", "is_public", "last_modified"]
    )
    
    return result

# 查询carrier_transport项目的contributions
contributions = query_contributions_by_project("carrier_transport", limit=200)
print(f"获取到 {len(contributions)} 个contributions")
```

**API参数详解**：
- `query`: 字典格式的查询条件，`{"project": "项目名称"}`
- `limit`: 限制返回结果数量，默认为25
- `fields`: 指定返回的字段，优化性能
- 返回结果是contributions列表

### 第5步：处理查询结果

```python
def process_contributions(contributions):
    """处理contributions查询结果"""
    
    if not contributions:
        print("没有找到contributions")
        return
    
    print(f"📊 统计信息:")
    print(f"   总数: {len(contributions)}")
    
    print(f"\n🔍 前5个contributions:")
    for i, contrib in enumerate(contributions[:5], 1):
        identifier = contrib.get("identifier", "N/A")
        formula = contrib.get("formula", "N/A")
        is_public = contrib.get("is_public", False)
        last_modified = contrib.get("last_modified", "N/A")
        
        print(f"   {i}. {identifier}")
        print(f"      - 化学式: {formula}")
        print(f"      - 公开状态: {'公开' if is_public else '私有'}")
        print(f"      - 最后修改: {last_modified}")
        print()

# 处理结果
process_contributions(contributions)
```

### 第6步：获取单个Contribution的详细信息

```python
def get_contribution_details(contribution_id):
    """获取特定contribution的详细信息"""
    
    try:
        # 使用内部ID获取详细信息
        detailed_info = mpr.contribs.get_contribution(contribution_id)
        
        print(f"📋 Contribution详细信息:")
        print(f"   ID: {detailed_info.get('id')}")
        print(f"   材料ID: {detailed_info.get('identifier')}")
        print(f"   化学式: {detailed_info.get('formula')}")
        print(f"   项目: {detailed_info.get('project')}")
        
        # 显示数据内容
        data = detailed_info.get('data', {})
        if data:
            print(f"   数据字段: {list(data.keys())}")
        
        return detailed_info
        
    except Exception as e:
        print(f"获取详细信息失败: {e}")
        return None

# 获取第一个contribution的详细信息
if contributions:
    first_contrib = contributions[0]
    contrib_id = first_contrib.get('id')
    details = get_contribution_details(contrib_id)
```

---

## 代码实现

### 完整的查询类实现

```python
class ContributionsQueryTool:
    """Contributions查询工具类"""
    
    def __init__(self, api_key):
        self.mpr = MPRester(api_key=api_key)
    
    def find_project_by_name(self, project_name):
        """步骤1: 根据名称查找项目"""
        projects = self.mpr.contribs.query_projects(
            fields=["name", "title", "description"]
        )
        
        for project in projects:
            if project.get("name") == project_name:
                return project
        return None
    
    def query_project_contributions(self, project_name, limit=100):
        """步骤2: 查询项目的contributions"""
        query_params = {"project": project_name}
        
        return self.mpr.contribs.query_contributions(
            query=query_params,
            limit=limit,
            fields=["identifier", "formula", "project", "is_public", "last_modified", "id"]
        )
    
    def get_contribution_details(self, contribution_id):
        """步骤3: 获取contribution详细信息"""
        return self.mpr.contribs.get_contribution(contribution_id)
    
    def complete_query_workflow(self, project_name, limit=100, show_details=True):
        """完整的查询工作流程"""
        print(f"🔍 开始查询项目: {project_name}")
        print("="*50)
        
        # 步骤1: 验证项目存在
        print("步骤1: 查找项目...")
        project = self.find_project_by_name(project_name)
        
        if not project:
            print(f"❌ 项目 '{project_name}' 未找到")
            return None
        
        print(f"✅ 找到项目: {project.get('name')} - {project.get('title')}")
        
        # 步骤2: 查询contributions
        print(f"\n步骤2: 查询contributions (限制: {limit})...")
        contributions = self.query_project_contributions(project_name, limit)
        
        if not contributions:
            print("❌ 没有找到contributions")
            return None
        
        print(f"✅ 找到 {len(contributions)} 个contributions")
        
        # 步骤3: 显示统计信息
        print(f"\n📊 统计信息:")
        print(f"   项目标题: {project.get('title')}")
        print(f"   项目描述: {project.get('description', 'N/A')[:100]}...")
        print(f"   contributions数量: {len(contributions)}")
        
        # 步骤4: 显示示例数据
        print(f"\n🔍 前3个contributions:")
        for i, contrib in enumerate(contributions[:3], 1):
            print(f"   {i}. {contrib.get('identifier')} ({contrib.get('formula')})")
        
        # 步骤5: 获取详细信息（可选）
        if show_details and contributions:
            print(f"\n📋 第一个contribution的详细信息:")
            first_contrib = contributions[0]
            details = self.get_contribution_details(first_contrib.get('id'))
            
            if details:
                data_keys = list(details.get('data', {}).keys())
                print(f"   数据字段: {data_keys[:5]}")  # 显示前5个字段
        
        return {
            "project": project,
            "contributions": contributions,
            "total_count": len(contributions)
        }

# 使用示例
tool = ContributionsQueryTool("你的API密钥")
result = tool.complete_query_workflow("carrier_transport", limit=50)
```

---

## 实际演示

### 演示脚本

```python
#!/usr/bin/env python3
"""
Contributions查询演示脚本
演示完整的查询流程
"""

def demo_query_process():
    """演示完整查询过程"""
    
    # 1. 初始化
    print("🚀 Material Project Contributions查询演示")
    print("="*60)
    
    api_key = "zNYpCJC5SulZoPratZXccTSOdNkXoqMb"  # 你的API密钥
    tool = ContributionsQueryTool(api_key)
    
    # 2. 演示不同项目的查询
    test_projects = [
        "carrier_transport",     # 载流子传输
        "2dmatpedia",           # 二维材料
        "hubbard"               # Hubbard参数
    ]
    
    for project_name in test_projects:
        print(f"\n{'='*30}")
        print(f"演示项目: {project_name}")
        print(f"{'='*30}")
        
        result = tool.complete_query_workflow(
            project_name, 
            limit=20, 
            show_details=False
        )
        
        if result:
            print(f"✅ 查询成功，找到 {result['total_count']} 个contributions")
        else:
            print("❌ 查询失败")
        
        input("\n按Enter继续下一个项目...")
    
    print(f"\n🎉 演示完成！")

if __name__ == "__main__":
    demo_query_process()
```

---

## 常见问题

### Q1: 为什么项目名称找不到？

**A**: 项目名称必须精确匹配，常见问题：
- 大小写敏感：`Carrier Transport` ≠ `carrier_transport`
- 显示名称 ≠ API名称：显示"Carrier Transport"，API名称是"carrier_transport"
- 特殊字符：空格通常被下划线替代

**解决方法**：
```python
# 先列出所有项目名称
projects = mpr.contribs.query_projects(fields=["name", "title"])
for p in projects:
    print(f"API名称: {p.get('name')} | 显示名称: {p.get('title')}")
```

### Q2: 为什么contributions数量不对？

**A**: 可能的原因：
- `limit` 参数限制了返回数量
- 查询条件过滤了部分结果
- API分页机制

**解决方法**：
```python
# 获取所有数据（分页查询）
all_contributions = []
limit = 1000
offset = 0

while True:
    batch = mpr.contribs.query_contributions(
        query={"project": "carrier_transport"},
        limit=limit,
        offset=offset
    )
    
    if not batch:
        break
    
    all_contributions.extend(batch)
    offset += limit
    
    if len(batch) < limit:  # 最后一页
        break

print(f"总共获取到 {len(all_contributions)} 个contributions")
```

### Q3: 如何获取所有字段信息？

**A**: 不指定`fields`参数获取完整数据：
```python
# 获取完整数据
contributions = mpr.contribs.query_contributions(
    query={"project": "carrier_transport"},
    limit=10
    # 不指定fields参数
)

# 查看可用字段
if contributions:
    print("可用字段:", list(contributions[0].keys()))
```

---

## 进阶技巧

### 1. 批量查询多个项目

```python
def batch_query_projects(project_names, limit_per_project=50):
    """批量查询多个项目的contributions"""
    results = {}
    
    for project_name in project_names:
        print(f"查询项目: {project_name}")
        
        contributions = mpr.contribs.query_contributions(
            query={"project": project_name},
            limit=limit_per_project
        )
        
        results[project_name] = {
            "count": len(contributions),
            "contributions": contributions
        }
        
        print(f"  -> 找到 {len(contributions)} 个contributions")
    
    return results

# 使用示例
projects = ["carrier_transport", "2dmatpedia", "hubbard"]
results = batch_query_projects(projects)
```

### 2. 条件查询contributions

```python
def query_contributions_with_conditions(project_name, conditions=None):
    """带条件的contributions查询"""
    
    query_params = {"project": project_name}
    
    # 添加额外查询条件
    if conditions:
        query_params.update(conditions)
    
    contributions = mpr.contribs.query_contributions(
        query=query_params,
        limit=1000
    )
    
    return contributions

# 示例：查询公开的contributions
public_contributions = query_contributions_with_conditions(
    "carrier_transport",
    conditions={"is_public": True}
)
```

### 3. 数据导出和保存

```python
import json
import pandas as pd

def export_contributions(contributions, format="json"):
    """导出contributions数据"""
    
    if format == "json":
        with open("contributions.json", "w") as f:
            json.dump(contributions, f, indent=2, default=str)
        print("数据已保存为 contributions.json")
    
    elif format == "csv":
        # 展平数据结构
        flattened = []
        for contrib in contributions:
            row = {
                "id": contrib.get("id"),
                "identifier": contrib.get("identifier"),
                "formula": contrib.get("formula"),
                "project": contrib.get("project"),
                "is_public": contrib.get("is_public"),
                "last_modified": contrib.get("last_modified")
            }
            flattened.append(row)
        
        df = pd.DataFrame(flattened)
        df.to_csv("contributions.csv", index=False)
        print("数据已保存为 contributions.csv")

# 使用示例
contributions = query_contributions_by_project("carrier_transport", limit=100)
export_contributions(contributions, format="csv")
```

---

## 总结

通过本教程，你已经学会了：

1. **理论基础**: Material Project Contributions的数据结构和查询原理
2. **实践技能**: 从项目名称到contributions的完整查询流程
3. **代码实现**: 可复用的查询工具类和函数
4. **问题解决**: 常见问题的诊断和解决方法
5. **进阶应用**: 批量查询、条件筛选、数据导出等高级功能

### 🎯 关键要点回顾

- 使用 `MPRester` 而不是 `mpcontribs.client.Client`
- 项目名称必须精确匹配API格式
- 查询参数格式：`{"project": "项目名称"}`
- 注意分页和限制参数
- 合理处理查询结果和错误情况

现在你已经掌握了完整的查询技能，可以轻松查询任何Material Project Contributions项目的数据！ 