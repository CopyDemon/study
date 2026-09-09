#!/usr/bin/env python3
"""
Material Project Contributions 分步演示脚本

这个脚本会一步一步演示如何通过项目名称查询到其contributions，
每个步骤都会暂停并解释发生了什么。

运行方式: python 分步演示脚本.py
"""

from mp_api.client import MPRester
import time

def pause_with_message(message):
    """显示消息并暂停"""
    print(f"\n{'='*60}")
    print(f"⏸️  {message}")
    print(f"{'='*60}")
    input("按Enter键继续...")

def step_by_step_demo():
    """分步演示查询过程"""
    
    print("🚀 Material Project Contributions 分步演示")
    print("本演示将展示如何从项目名称查询到contributions的完整过程")
    print("\n我们将以 'Carrier Transport' 项目为例进行演示")
    
    pause_with_message("准备开始演示，我们将学习6个关键步骤")
    
    # ============================================================================
    # 步骤1: 初始化API客户端
    # ============================================================================
    print("\n" + "🔸"*60)
    print("步骤1: 初始化API客户端")
    print("🔸"*60)
    
    print("正在初始化Material Project API客户端...")
    print("使用的包: from mp_api.client import MPRester")
    
    # 实际代码
    api_key = "zNYpCJC5SulZoPratZXccTSOdNkXoqMb"
    mpr = MPRester(api_key=api_key)
    
    print("✅ API客户端初始化成功")
    print(f"   - 使用的API密钥: {api_key[:20]}...")
    print(f"   - 客户端类型: {type(mpr)}")
    
    pause_with_message("步骤1完成！我们已经创建了API客户端，可以与Material Project通信")
    
    # ============================================================================
    # 步骤2: 查询所有可用项目
    # ============================================================================
    print("\n" + "🔸"*60)
    print("步骤2: 查询所有可用项目")
    print("🔸"*60)
    
    print("正在查询所有可用的contributions项目...")
    print("API调用: mpr.contribs.query_projects()")
    
    # 实际代码
    projects = mpr.contribs.query_projects(fields=["name", "title", "description"])
    
    print(f"✅ 查询成功！找到 {len(projects)} 个项目")
    print("\n📋 前10个项目示例:")
    for i, project in enumerate(projects[:10], 1):
        name = project.get("name", "N/A")
        title = project.get("title", "N/A")
        print(f"   {i:2d}. {name:<25} - {title}")
    
    print("...")
    print(f"   (还有 {len(projects)-10} 个项目)")
    
    pause_with_message("步骤2完成！我们看到了所有可用项目。注意项目的API名称和显示标题可能不同")
    
    # ============================================================================
    # 步骤3: 根据名称查找特定项目
    # ============================================================================
    print("\n" + "🔸"*60)
    print("步骤3: 根据名称查找特定项目")
    print("🔸"*60)
    
    target_project_name = "carrier_transport"
    print(f"目标项目名称: '{target_project_name}'")
    print("搜索策略: 遍历所有项目，查找名称匹配的项目")
    
    # 实际代码
    found_project = None
    for project in projects:
        if project.get("name") == target_project_name:
            found_project = project
            break
    
    if found_project:
        print("✅ 找到目标项目！")
        print(f"   - API名称: {found_project.get('name')}")
        print(f"   - 显示标题: {found_project.get('title')}")
        print(f"   - 描述: {found_project.get('description', 'N/A')[:100]}...")
    else:
        print("❌ 未找到项目")
        return
    
    pause_with_message("步骤3完成！我们成功找到了Carrier Transport项目")
    
    # ============================================================================
    # 步骤4: 构建查询参数并查询contributions
    # ============================================================================
    print("\n" + "🔸"*60)
    print("步骤4: 查询项目的contributions")
    print("🔸"*60)
    
    print("构建查询参数...")
    
    # 实际代码
    query_params = {
        "project": target_project_name  # 关键：使用project参数筛选
    }
    
    print(f"查询参数: {query_params}")
    print("API调用: mpr.contribs.query_contributions()")
    print("正在执行查询...")
    
    contributions = mpr.contribs.query_contributions(
        query=query_params,
        fields=["identifier", "formula", "project", "is_public", "last_modified", "id"]
    )
    
    # 处理结果 - 可能返回字典格式
    if isinstance(contributions, dict):
        contributions_list = contributions.get('data', [])
        total_available = contributions.get('total_doc', len(contributions_list))
        print(f"✅ 查询成功！获取到 {len(contributions_list)} 个contributions (总计: {total_available})")
        contributions = contributions_list[:100]  # 取前100个用于演示
    else:
        contributions = contributions[:100] if len(contributions) > 100 else contributions
        print(f"✅ 查询成功！获取到 {len(contributions)} 个contributions")
    
    print(f"   - 演示数量: {len(contributions)}个")
    print(f"   - 数据类型: {type(contributions)}")
    
    pause_with_message("步骤4完成！我们成功查询到了contributions数据")
    
    # ============================================================================
    # 步骤5: 分析和展示查询结果
    # ============================================================================
    print("\n" + "🔸"*60)
    print("步骤5: 分析和展示查询结果")
    print("🔸"*60)
    
    if contributions:
        print("📊 数据统计分析:")
        print(f"   - 总数量: {len(contributions)}")
        
        # 分析数据结构
        first_contrib = contributions[0]
        print(f"   - 数据字段: {list(first_contrib.keys())}")
        
        # 分析公开性
        public_count = sum(1 for c in contributions if c.get('is_public', False))
        print(f"   - 公开数据: {public_count}/{len(contributions)}")
        
        print(f"\n🔍 前5个contributions详情:")
        for i, contrib in enumerate(contributions[:5], 1):
            identifier = contrib.get("identifier", "N/A")
            formula = contrib.get("formula", "N/A")
            is_public = contrib.get("is_public", False)
            last_modified = contrib.get("last_modified", "N/A")
            internal_id = contrib.get("id", "N/A")
            
            print(f"\n   📄 Contribution {i}:")
            print(f"      - Material ID: {identifier}")
            print(f"      - 化学式: {formula}")
            print(f"      - 内部ID: {internal_id}")
            print(f"      - 公开状态: {'✅ 公开' if is_public else '🔒 私有'}")
            print(f"      - 最后修改: {str(last_modified)[:19]}")
    
    pause_with_message("步骤5完成！我们分析了查询结果，看到了contributions的基本信息")
    
    # ============================================================================
    # 步骤6: 获取详细信息（可选）
    # ============================================================================
    print("\n" + "🔸"*60)
    print("步骤6: 获取单个contribution的详细信息")
    print("🔸"*60)
    
    if contributions:
        first_contrib = contributions[0]
        contrib_id = first_contrib.get('id')
        
        print(f"选择第一个contribution进行详细查询:")
        print(f"   - Material ID: {first_contrib.get('identifier')}")
        print(f"   - 内部ID: {contrib_id}")
        
        print("\nAPI调用: mpr.contribs.get_contribution()")
        print("正在获取详细信息...")
        
        try:
            # 实际代码
            detailed_info = mpr.contribs.get_contribution(contrib_id)
            
            print("✅ 详细信息获取成功！")
            print(f"\n📋 详细信息结构:")
            print(f"   - 基本字段: {list(detailed_info.keys())}")
            
            # 显示数据内容
            data_section = detailed_info.get('data', {})
            if data_section:
                print(f"   - 数据字段: {list(data_section.keys())[:10]}...")  # 显示前10个字段
                print(f"   - 数据字段总数: {len(data_section)}")
            else:
                print("   - 无详细数据内容")
                
        except Exception as e:
            print(f"❌ 获取详细信息失败: {e}")
    
    pause_with_message("步骤6完成！我们成功获取了单个contribution的详细信息")
    
    # ============================================================================
    # 总结
    # ============================================================================
    print("\n" + "🎉"*60)
    print("🎉 演示完成！总结学习成果")
    print("🎉"*60)
    
    print("\n📚 我们学到了什么:")
    print("1. 📡 初始化API客户端: MPRester(api_key)")
    print("2. 📋 查询所有项目: mpr.contribs.query_projects()")
    print("3. 🔍 查找特定项目: 遍历projects列表匹配name字段")
    print("4. ⚡ 查询contributions: mpr.contribs.query_contributions(query={})")
    print("5. 📊 分析结果数据: 统计、展示、字段分析")
    print("6. 🔬 获取详细信息: mpr.contribs.get_contribution(id)")
    
    print(f"\n🎯 关键技术点:")
    print("✅ 使用 MPRester 而不是 mpcontribs.client.Client")
    print("✅ 项目名称精确匹配 (carrier_transport ≠ Carrier Transport)")
    print("✅ 查询参数格式: {'project': 'project_name'}")
    print("✅ 合理使用limit参数控制数据量")
    print("✅ 区分内部ID和Material Project ID")
    
    print(f"\n📈 查询结果统计:")
    if 'contributions' in locals():
        print(f"   - 项目: {found_project.get('title')}")
        print(f"   - 查询到的数据: {len(contributions)} 个contributions")
        print(f"   - 成功演示: 完整的查询流程")
    
    print("\n🚀 现在你已经掌握了完整的查询技能！")
    print("   可以使用相同的方法查询任何Material Project Contributions项目")

def quick_demo():
    """快速演示版本（无暂停）"""
    print("🚀 快速演示版本")
    print("="*50)
    
    # 快速执行所有步骤
    api_key = "zNYpCJC5SulZoPratZXccTSOdNkXoqMb"
    mpr = MPRester(api_key=api_key)
    
    projects = mpr.contribs.query_projects(fields=["name", "title"])
    print(f"1. 找到 {len(projects)} 个项目")
    
    target_project = None
    for project in projects:
        if project.get("name") == "carrier_transport":
            target_project = project
            break
    
    if target_project:
        print(f"2. 找到项目: {target_project.get('title')}")
        
        contributions = mpr.contribs.query_contributions(
            query={"project": "carrier_transport"}
        )
        
        # 处理结果格式
        if isinstance(contributions, dict):
            contributions_list = contributions.get('data', [])
            total_count = contributions.get('total_doc', len(contributions_list))
            print(f"3. 查询到 {len(contributions_list)} 个contributions (总计: {total_count})")
            if contributions_list:
                print(f"4. 示例: {contributions_list[0].get('identifier')} - {contributions_list[0].get('formula')}")
        else:
            print(f"3. 查询到 {len(contributions)} 个contributions")
            if contributions:
                print(f"4. 示例: {contributions[0].get('identifier')} - {contributions[0].get('formula')}")
        
        print("✅ 快速演示完成！")

if __name__ == "__main__":
    print("选择演示模式:")
    print("1. 详细分步演示 (推荐学习)")
    print("2. 快速演示")
    
    choice = input("请输入选择 (1/2): ").strip()
    
    if choice == "2":
        quick_demo()
    else:
        step_by_step_demo() 