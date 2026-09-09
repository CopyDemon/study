#!/usr/bin/env python3
"""
Material Project Contributions 快速查询演示

这个脚本展示如何快速查询特定项目的contributions数据。

使用方法:
    python 查询项目演示.py

作者: AI助手
日期: 2024年
"""

from api_key.load_api_key import Load_API_Key
from api_playground.contribs_api import MPContribsClient

def main():
    """主演示函数"""
    print("🚀 Material Project Contributions 快速查询演示")
    print("=" * 60)
    
    # 初始化API客户端
    # MP_API_KEY = Load_API_Key("MP_API_KEY").get_key()
    MP_API_KEY = "zNYpCJC5SulZoPratZXccTSOdNkXoqMb"
    client = MPContribsClient(MP_API_KEY)
    
    # 演示不同项目的查询
    projects_to_demo = [
        ("carrier_transport", "载流子传输数据"),
        ("2dmatpedia", "二维材料数据库"),
        ("defect_genome_pcfc_materials", "缺陷基因组PCFC材料"),
        ("esters", "酯类化合物"),
        ("hubbard", "Hubbard U和J数据库")
    ]
    
    for i, (project_name, description) in enumerate(projects_to_demo, 1):
        print(f"\n📋 演示 {i}: {description}")
        print("-" * 40)
        
        # 使用便捷函数查询项目
        result = client.quick_project_query(project_name, num_examples=3)
        
        if result["success"]:
            print(f"🎯 项目查询成功完成!\n")
        else:
            print(f"❌ 查询失败: {result.get('error', '未知错误')}\n")
        
        # 添加分隔符
        if i < len(projects_to_demo):
            input("按Enter键继续查询下一个项目...")
    
    print("\n" + "=" * 60)
    print("✅ 所有演示完成!")
    print("\n💡 使用提示:")
    print("   1. 使用 client.quick_project_query('项目名') 快速查询任何项目")
    print("   2. 项目名称必须是准确的英文名称，如 'carrier_transport'")
    print("   3. 返回的结果包含项目统计信息和示例数据")
    print("   4. 可以通过 num_examples 参数控制返回的示例数量")
    
    print("\n🔍 常用项目名称:")
    common_projects = [
        "carrier_transport - 载流子传输数据 (47,737个contributions)",
        "2dmatpedia - 二维材料数据库",
        "defect_genome_pcfc_materials - 缺陷基因组PCFC材料",
        "hubbard - Hubbard U和J数据库",
        "experimental_thermo - 热化学数据"
    ]
    
    for project in common_projects:
        print(f"   • {project}")

def quick_query_example():
    """简单的快速查询示例"""
    print("\n🎯 快速查询示例:")
    print("=" * 30)
    
    # 初始化客户端
    MP_API_KEY = "zNYpCJC5SulZoPratZXccTSOdNkXoqMb"
    client = MPContribsClient(MP_API_KEY)
    
    # 查询Carrier Transport项目
    print("查询Carrier Transport项目:")
    result = client.quick_project_query("carrier_transport", num_examples=2)
    
    if result["success"]:
        print(f"\n📊 总结:")
        print(f"   - 项目: {result['project_title']}")
        print(f"   - 总数: {result['total_count']:,} 个contributions")
        print(f"   - 包含载流子传输性质的DFT计算数据")

if __name__ == "__main__":
    # 运行完整演示
    main()
    
    # 或者只运行快速示例
    # quick_query_example() 