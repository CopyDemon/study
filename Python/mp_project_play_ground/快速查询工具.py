#!/usr/bin/env python3
"""
快速查询Material Project Contributions工具

这个脚本提供一个简单的函数来快速查询任何项目的contributions数据。

使用示例:
    # 查询Carrier Transport项目
    query_project("carrier_transport")
    
    # 查询其他项目
    query_project("2dmatpedia", num_examples=10)

作者: AI助手
"""

from api_key.load_api_key import Load_API_Key
from api_playground.contribs_api import MPContribsClient

# 全局客户端实例
_client = None

def init_client():
    """初始化API客户端"""
    global _client
    if _client is None:
        # MP_API_KEY = Load_API_Key("MP_API_KEY").get_key()
        MP_API_KEY = "zNYpCJC5SulZoPratZXccTSOdNkXoqMb"
        _client = MPContribsClient(MP_API_KEY)
    return _client

def query_project(project_name: str, num_examples: int = 5):
    """
    快速查询指定项目的contributions
    
    Args:
        project_name (str): 项目名称，例如:
            - "carrier_transport" (载流子传输)
            - "2dmatpedia" (二维材料)
            - "defect_genome_pcfc_materials" (缺陷基因组)
        num_examples (int): 显示的示例数量，默认5个
    
    Returns:
        dict: 查询结果，包含项目信息和示例数据
        
    Example:
        >>> result = query_project("carrier_transport")
        >>> print(f"项目有 {result['total_count']} 个contributions")
    """
    client = init_client()
    return client.quick_project_query(project_name, num_examples)

def list_common_projects():
    """显示常用项目列表"""
    print("📋 常用项目名称:")
    projects = [
        ("carrier_transport", "载流子传输数据", "47,737个contributions"),
        ("2dmatpedia", "二维材料数据库", "包含二维材料性质"),
        ("defect_genome_pcfc_materials", "缺陷基因组PCFC材料", "材料缺陷计算"),
        ("hubbard", "Hubbard U和J数据库", "强关联电子材料"),
        ("experimental_thermo", "热化学数据", "实验热力学数据"),
        ("esters", "酯类化合物", "有机化合物数据"),
        ("dielectric_piezoelectric", "介电压电数据", "介电和压电性质"),
        ("friction", "摩擦数据", "摩擦系数计算")
    ]
    
    for name, desc, note in projects:
        print(f"   • {name:<25} - {desc} ({note})")

def search_projects_by_keyword(keyword: str):
    """根据关键词搜索项目"""
    client = init_client()
    all_names = client.list_all_project_names()
    
    matches = [name for name in all_names if keyword.lower() in name.lower()]
    
    print(f"🔍 包含关键词 '{keyword}' 的项目:")
    for name in matches[:10]:  # 最多显示10个
        print(f"   • {name}")
    
    if len(matches) > 10:
        print(f"   ... 还有 {len(matches) - 10} 个项目")

# 快捷函数
def carrier_transport(num_examples=5):
    """快速查询Carrier Transport项目"""
    return query_project("carrier_transport", num_examples)

def two_d_materials(num_examples=5):
    """快速查询2DMatPedia项目"""
    return query_project("2dmatpedia", num_examples)

def defect_genome(num_examples=5):
    """快速查询Defect Genome项目"""
    return query_project("defect_genome_pcfc_materials", num_examples)

if __name__ == "__main__":
    print("🚀 Material Project Contributions 快速查询工具")
    print("=" * 50)
    
    # 显示使用说明
    print("\n💡 使用方法:")
    print("1. 直接查询项目:")
    print("   query_project('carrier_transport')")
    print("   query_project('2dmatpedia', num_examples=10)")
    print("\n2. 使用快捷函数:")
    print("   carrier_transport()  # 查询载流子传输项目")
    print("   two_d_materials()    # 查询二维材料项目")
    print("\n3. 搜索项目:")
    print("   search_projects_by_keyword('transport')")
    
    # 显示常用项目
    print("\n" + "=" * 50)
    list_common_projects()
    
    # 演示查询Carrier Transport
    print("\n" + "=" * 50)
    print("🎯 演示: 查询Carrier Transport项目")
    print("-" * 30)
    
    result = carrier_transport(num_examples=3)
    
    if result["success"]:
        print(f"\n📊 快速总结:")
        print(f"   项目: {result['project_title']}")
        print(f"   数据量: {result['total_count']:,} 个contributions")
        print(f"   示例: 显示了 {result['sample_count']} 个")
        print(f"\n   💡 这个项目包含DFT计算的载流子传输性质数据，")
        print(f"      如电子/空穴有效质量、载流子迁移率等。")
    else:
        print(f"❌ 查询失败: {result.get('error')}")
    
    print("\n✅ 工具演示完成!")
    print("现在可以使用 query_project() 函数查询任何项目了。") 