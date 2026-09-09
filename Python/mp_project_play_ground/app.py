from api_key.load_api_key import Load_API_Key
from api_playground.contribs_api import MPContribsClient
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


print("This is Material project play ground")
print("To check each sub-folders to discover demo")

########################################################
# API CALLS
########################################################
# load api key
# MP_API_KEY = Load_API_Key("MP_API_KEY").get_key()
MP_API_KEY = "zNYpCJC5SulZoPratZXccTSOdNkXoqMb"

# 创建客户端实例
client = MPContribsClient(MP_API_KEY)

# show available resources for mpr(MPRester) and mpr(MPRester) contribs
client.show_available_resources_for_mpr()
# show available resources for mpr(MPRester) contribs
client.show_available_resources_for_mpr_contribs()

# query projects
projects = client.query_projects()

# query all contribs ids
# client.query_all_contribs_ids()

########################################################
# 查询特定项目的contributions示例
########################################################
print("\n" + "="*60)
print("查询特定项目的contributions示例")
print("="*60)

# 首先检查API方法的正确参数
print("\n🔍 检查query_contributions方法的参数...")
client.inspect_query_contributions_method()

print("\n📋 检查可用的查询参数...")
client.check_available_query_params()

print("\n📋 获取示例contributions数据...")
sample_contributions = client.get_sample_contributions(count=3)

# 然后显示前10个项目名称
print("\n📋 显示前10个可用项目:")
project_names = client.list_all_project_names(limit=10)

# 选择第一个项目进行测试
if project_names:
    project_name = project_names[0]  # 使用第一个项目
    print(f"\n🎯 选择项目进行测试: {project_name}")
    
    # 1. 首先查找项目信息
    project_info = client.find_project_by_name(project_name)
    if project_info:
        print(f"✅ 找到项目: {project_info.get('name')} (ID: {project_info.get('project_id')})")
        
        # 2. 查询该项目的所有contributions
        contributions = client.query_contributions_by_project_name(project_name, limit=20)
        
        if contributions:
            print(f"\n📊 项目统计:")
            print(f"   - 总contributions数: {len(contributions)}")
            
            # 3. 显示第一个contribution的详细信息（使用正确的内部ID）
            if contributions:
                first_contrib = contributions[0]
                contribution_id = first_contrib.get('id')  # 使用内部ID，不是identifier
                identifier = first_contrib.get('identifier', 'N/A')
                
                print(f"\n🔍 查看第一个contribution的详细信息 (Material ID: {identifier}):")
                print(f"   内部ID: {contribution_id}")
                
                detailed_info = client.get_detailed_contribution_info(project_name, contribution_id)
        else:
            print("❌ 该项目没有找到contributions")
    else:
        print(f"❌ 未找到项目: {project_name}")
else:
    print("❌ 没有找到任何项目")

print("\n" + "="*60)
print("💡 使用说明:")
print("   现在我们知道了API的正确用法，可以根据上面的信息")
print("   来正确查询特定项目的contributions")
print("="*60)

########################################################
# 演示: 查询Carrier Transport项目的contributions
########################################################
print("\n" + "="*60)
print("📋 演示: 查询Carrier Transport项目的contributions")
print("="*60)

# 查询Carrier Transport项目
carrier_transport_summary = client.query_project_contributions_summary("carrier_transport", sample_size=3)

if carrier_transport_summary and carrier_transport_summary.get("success"):
    total = carrier_transport_summary.get("total_contributions", 0)
    print(f"\n🎯 Carrier Transport项目总结:")
    print(f"   - 总共有 {total:,} 个contributions")
    print(f"   - 这些contributions包含了载流子传输性质的计算数据")
    print(f"   - 每个contribution对应一个材料(Material Project ID)")
    
    # 如果用户想要获取特定contribution的详细信息
    sample_contributions = carrier_transport_summary.get("sample_contributions", [])
    if sample_contributions:
        first_contrib = sample_contributions[0]
        contrib_id = first_contrib.get('id')
        identifier = first_contrib.get('identifier')
        
        print(f"\n🔍 获取第一个contribution的详细信息:")
        print(f"   Material ID: {identifier}")
        detailed_info = client.get_detailed_contribution_info("carrier_transport", contrib_id)
        
        if detailed_info:
            print(f"\n✅ 成功获取详细信息！")
        else:
            print(f"\n❌ 获取详细信息失败")

print("\n" + "="*60)
print("📝 使用总结:")
print("   1. 使用 client.query_project_contributions_summary('项目名') 查询项目概况")
print("   2. 使用 client.get_detailed_contribution_info('项目名', '内部ID') 获取详细信息")
print("   3. Carrier Transport项目包含 47,737 个材料的载流子传输数据")
print("="*60)
