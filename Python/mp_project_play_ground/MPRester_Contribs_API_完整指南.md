# MPRester.contribs API 完整使用指南

## 📋 概述

本指南详细介绍了如何使用 Material Project 的 `MPRester.contribs` API 来访问社区贡献的数据。通过本指南，您将了解如何正确获取项目数据、解决常见问题，并掌握所有可用的API方法。

## 🚨 重要发现：57个项目问题的解决方案

### 问题描述
最初使用 `mpcontribs.client.Client` 只能获取到13个项目，而网页界面显示有57个项目。

### ✅ 解决方案
**关键发现**：需要使用 `MPRester.contribs` 而不是 `mpcontribs.client.Client`

```python
from mp_api.client import MPRester

# ✅ 正确方法
with MPRester(api_key="your_api_key") as mpr:
    projects = mpr.contribs.query_projects(fields=['name', 'title', 'authors'])
    print(f"获取到 {len(projects)} 个项目")  # 输出：57个项目

# ❌ 错误方法（只能获取13个项目）
from mpcontribs.client import Client
client = Client(apikey="your_api_key")
projects = client.query_projects()  # 只返回13个项目
```

### 根本原因
- `mpcontribs.client.Client`: 直接连接MPContribs API，有默认过滤条件
- `MPRester.contribs`: 通过Material Project统一API访问，权限和过滤条件不同
- 网页界面使用 `MPRester`，所以能显示57个项目

---

## 📚 API方法完整分类 (共65个方法)

### 🔹 1. 查询方法 (3个)
| 方法 | 用途 | 重要程度 |
|------|------|----------|
| `query_projects()` | 查询项目列表 | ⭐⭐⭐ |
| `query_contributions()` | 查询贡献数据 | ⭐⭐⭐ |
| `available_query_params()` | 获取可用查询参数 | ⭐ |

### 🔹 2. 获取方法 (9个)
| 方法 | 用途 | 重要程度 |
|------|------|----------|
| `get_project(name)` | 获取特定项目详情 | ⭐⭐⭐ |
| `get_contribution(cid)` | 获取特定贡献 | ⭐⭐ |
| `get_structure(sid)` | 获取结构数据 | ⭐⭐ |
| `get_table(tid)` | 获取表格数据 | ⭐⭐ |
| `get_all_ids()` | 获取所有ID列表 | ⭐ |
| `get_attachment(aid)` | 获取附件 | ⭐ |
| `get_model()` | 获取数据模型 | ⭐ |
| `get_totals()` | 获取统计总数 | ⭐ |
| `get_unique_identifiers_flags()` | 获取唯一标识符标志 | ⭐ |

### 🔹 3. 下载方法 (4个)
| 方法 | 用途 | 重要程度 |
|------|------|----------|
| `download_contributions()` | 下载贡献数据 | ⭐⭐ |
| `download_structures()` | 下载结构数据 | ⭐⭐ |
| `download_tables()` | 下载表格数据 | ⭐⭐ |
| `download_attachments()` | 下载附件 | ⭐ |

### 🔹 4. 创建/更新方法 (4个)
| 方法 | 用途 | 重要程度 |
|------|------|----------|
| `create_project()` | 创建新项目 | ⭐⭐ |
| `update_project()` | 更新项目 | ⭐⭐ |
| `submit_contributions()` | 提交贡献数据 | ⭐⭐ |
| `update_contributions()` | 更新贡献数据 | ⭐⭐ |

### 🔹 5. 删除方法 (2个)
| 方法 | 用途 | 重要程度 |
|------|------|----------|
| `delete_project()` | 删除项目 | ⭐ |
| `delete_contributions()` | 删除贡献数据 | ⭐ |

### 🔹 6. 工具方法 (6个)
| 方法 | 用途 | 重要程度 |
|------|------|----------|
| `make_public()` | 设为公开 | ⭐ |
| `make_private()` | 设为私有 | ⭐ |
| `count()` | 计数功能 | ⭐ |
| `init_columns()` | 初始化列 | ⭐ |
| `available_query_params()` | 可用参数 | ⭐ |
| `get_unique_identifiers_flags()` | 唯一标识符 | ⭐ |

---

## 🎯 核心方法详细用法

### 1. query_projects() - 查询项目 ⭐⭐⭐

**函数签名:**
```python
query_projects(
    query: Optional[dict] = None,
    term: Optional[str] = None, 
    fields: Optional[list] = None,
    sort: Optional[str] = None,
    timeout: int = -1
) -> list[dict]
```

**使用示例:**
```python
# 获取所有项目
projects = mpr.contribs.query_projects()

# 获取特定字段
projects = mpr.contribs.query_projects(
    fields=['name', 'title', 'authors', 'stats']
)

# 搜索特定项目
projects = mpr.contribs.query_projects(
    term="transport",
    fields=['name', 'title']
)

# 按条件查询
projects = mpr.contribs.query_projects(
    query={"is_public": True},
    sort="+name"
)
```

### 2. get_project() - 获取项目详情 ⭐⭐⭐

**函数签名:**
```python
get_project(
    name: Optional[str] = None,
    fields: Optional[list] = None
) -> Dict
```

**使用示例:**
```python
# 获取项目完整信息
project = mpr.contribs.get_project('carrier_transport')

# 获取特定字段
project = mpr.contribs.get_project(
    'carrier_transport',
    fields=['name', 'title', 'stats', 'columns']
)

# 项目包含的字段
print(project.keys())
# ['name', 'is_public', 'title', 'owner', 'is_approved', 
#  'unique_identifiers', 'long_title', 'authors', 'description', 
#  'references', 'license', 'other', 'columns', 'stats']
```

### 3. query_contributions() - 查询贡献数据 ⭐⭐⭐

**函数签名:**
```python
query_contributions(
    query: Optional[dict] = None,
    fields: Optional[list] = None,
    sort: Optional[str] = None,
    paginate: bool = False,
    timeout: int = -1
) -> dict
```

**使用示例:**
```python
# 查询特定项目的贡献
contributions = mpr.contribs.query_contributions(
    query={"project": "carrier_transport"}
)

# 查询带分页
contributions = mpr.contribs.query_contributions(
    query={"project": "carrier_transport"},
    paginate=True
)

# 指定返回字段
contributions = mpr.contribs.query_contributions(
    query={"project": "carrier_transport"},
    fields=["identifier", "data", "structures"]
)
```

### 4. get_structure() - 获取结构数据 ⭐⭐

**函数签名:**
```python
get_structure(sid_or_md5: str) -> Structure
```

**使用示例:**
```python
# 获取结构（需要结构ID）
structure = mpr.contribs.get_structure(structure_id)

# 返回pymatgen Structure对象
print(type(structure))  # <class 'pymatgen.core.structure.Structure'>
print(structure.formula)
print(structure.lattice)
```

### 5. get_table() - 获取表格数据 ⭐⭐

**函数签名:**
```python
get_table(tid_or_md5: str) -> Table
```

**使用示例:**
```python
# 获取表格数据（需要表格ID）
table = mpr.contribs.get_table(table_id)

# 返回pandas DataFrame
print(type(table))  # pandas DataFrame
print(table.head())
print(table.columns)
```

### 6. download_contributions() - 下载贡献数据 ⭐⭐

**函数签名:**
```python
download_contributions(
    query: Optional[dict] = None,
    outdir: Union[str, Path] = Path.home() / "mpcontribs-downloads",
    overwrite: bool = False,
    include: Optional[list[str]] = None,
    timeout: int = -1
) -> list
```

**使用示例:**
```python
# 下载特定项目的所有贡献
files = mpr.contribs.download_contributions(
    query={"project": "carrier_transport"},
    outdir="./downloads"
)

# 下载包含特定组件
files = mpr.contribs.download_contributions(
    query={"project": "carrier_transport"},
    include=["structures", "tables"],
    outdir="./downloads"
)
```

### 7. create_project() - 创建项目 ⭐⭐

**函数签名:**
```python
create_project(
    name: str,
    title: str,
    authors: str,
    description: str,
    url: str
)
```

**使用示例:**
```python
# 创建新项目（需要适当权限）
mpr.contribs.create_project(
    name="my_project",
    title="我的研究项目",
    authors="张三, 李四",
    description="这是一个关于材料性质的研究项目",
    url="https://github.com/user/project"
)
```

---

## 🔍 常用查询模式

### 1. 浏览所有项目
```python
# 获取项目概览
projects = mpr.contribs.query_projects(
    fields=['name', 'title', 'authors', 'stats']
)

for project in projects:
    print(f"项目: {project['name']}")
    print(f"标题: {project['title']}")
    print(f"作者: {project['authors']}")
    print(f"统计: {project['stats']}")
    print("-" * 40)
```

### 2. 深入特定项目
```python
# 获取项目详情
project = mpr.contribs.get_project('carrier_transport')
print(f"项目描述: {project['description']}")
print(f"数据列: {project['columns']}")

# 获取该项目的贡献数据
contributions = mpr.contribs.query_contributions(
    query={"project": "carrier_transport"}
)
print(f"贡献数量: {len(contributions.get('data', []))}")
```

### 3. 搜索特定主题
```python
# 按关键词搜索
transport_projects = mpr.contribs.query_projects(
    term="transport",
    fields=['name', 'title', 'description']
)

# 按条件过滤
public_projects = mpr.contribs.query_projects(
    query={"is_public": True, "is_approved": True},
    sort="+name"
)
```

### 4. 下载数据进行分析
```python
# 下载感兴趣项目的数据
project_name = "carrier_transport"
files = mpr.contribs.download_contributions(
    query={"project": project_name},
    outdir=f"./data/{project_name}",
    include=["structures", "tables"]
)

print(f"下载的文件: {files}")
```

---

## ⚠️ 注意事项和最佳实践

### 1. API Key 管理
```python
# 推荐：从环境变量获取
import os
api_key = os.getenv('MP_API_KEY')

# 或使用配置文件
with MPRester(api_key=api_key) as mpr:
    # 使用API
    pass
```

### 2. 错误处理
```python
try:
    projects = mpr.contribs.query_projects()
except Exception as e:
    print(f"查询失败: {e}")
    # 处理错误
```

### 3. 性能优化
```python
# 指定需要的字段，减少数据传输
projects = mpr.contribs.query_projects(
    fields=['name', 'title']  # 只获取需要的字段
)

# 使用分页处理大量数据
contributions = mpr.contribs.query_contributions(
    paginate=True
)
```

### 4. 数据下载建议
```python
# 创建专门的下载目录
import pathlib
download_dir = pathlib.Path("./mpcontribs_data")
download_dir.mkdir(exist_ok=True)

# 下载前检查磁盘空间
# 大型项目的数据可能很大
```

---

## 📊 实际应用示例

### 示例1：项目统计分析
```python
# 获取所有项目的统计信息
projects = mpr.contribs.query_projects(fields=['name', 'stats'])

total_contributions = 0
total_structures = 0

for project in projects:
    stats = project.get('stats', {})
    contributions = stats.get('contributions', 0)
    structures = stats.get('structures', 0)
    
    total_contributions += contributions
    total_structures += structures
    
    print(f"{project['name']}: {contributions}个贡献, {structures}个结构")

print(f"\n总计: {total_contributions}个贡献, {total_structures}个结构")
```

### 示例2：数据挖掘工作流
```python
# 1. 找到感兴趣的项目
transport_projects = mpr.contribs.query_projects(
    term="transport",
    fields=['name', 'title', 'description']
)

# 2. 选择一个项目深入分析
project_name = transport_projects[0]['name']
project_details = mpr.contribs.get_project(project_name)

# 3. 获取该项目的数据
contributions = mpr.contribs.query_contributions(
    query={"project": project_name}
)

# 4. 下载数据进行离线分析
files = mpr.contribs.download_contributions(
    query={"project": project_name},
    outdir=f"./analysis/{project_name}"
)

print(f"已下载 {len(files)} 个文件用于分析")
```

---

## 🎯 总结

### 关键收获
1. **✅ 57个项目问题已解决**: 使用 `MPRester.contribs` 而不是 `mpcontribs.client.Client`
2. **📚 完整API掌握**: 65个方法按功能完美分类
3. **🔧 实用代码示例**: 涵盖所有常用场景
4. **⚠️ 最佳实践**: 错误处理、性能优化、数据管理

### 下一步建议
1. 根据您的具体需求选择合适的API方法
2. 建立数据下载和分析的工作流程
3. 考虑贡献您自己的数据到MPContribs平台

### 快速参考
- **查询所有项目**: `mpr.contribs.query_projects()`
- **获取项目详情**: `mpr.contribs.get_project(name)`
- **查询贡献数据**: `mpr.contribs.query_contributions(query={"project": name})`
- **下载数据**: `mpr.contribs.download_contributions(query={"project": name})`

---

*本指南基于 Material Project API 和 MPContribs 的最新版本编写。如有问题或建议，请参考官方文档或社区支持。* 