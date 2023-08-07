import structura_core
import os
import shutil
import json

structura_core.debug=False
files_to_conver_path = "test.json"
# # 打开包含JSON数据的文件
# with open('tmpConver/'+"test.json", 'r') as file:
#     # 解析JSON数据
#     files_to_conver = json.load(file)
with open('tmpConver/'+files_to_conver_path, 'r') as file:
    # 解析JSON数据
    files_to_conver = json.load(file)


# files_to_conver = {
        
#         "gems":{"file":"test_structures/All Blocks World/gems and redstone.mcstructure",
#                 "offset":[-32,0,-32]},
#         "stone":{"file":"test_structures/All Blocks World/Stones.mcstructure",
#                  "offset":[-30,0,-32]},
#         "wood":{"file":"test_structures/All Blocks World/wood.mcstructure",
#                 "offset":[-31,0,-31]},
#         "decor":{"file":"test_structures/All Blocks World/decorative.mcstructure",
#                  "offset":[-32,0,-31]},
#         "wood2":{"file":"test_structures/All Blocks World/wood2.mcstructure",
#                  "offset":[-32,0,-31]}
#                  }
tempName = "sa"


try:
    shutil.rmtree("tmpPack/"+tempName+"/")
except:
    pass
if os.path.exists("tmpPack/"+tempName+"/"+tempName+".mcpack"):
    os.remove("tmpPack/"+tempName+"/"+tempName+".mcpack")
# if os.path.exists("tmp/all_blocks Nametags.txt"):
#     os.remove("tmp/all_blocks Nametags.txt")
    

# 目录+名字
structura_base=structura_core.structura("tmpPack/"+tempName+"/"+tempName)

# 透明度 20
structura_base.set_opacity(20)

for name_tag, info in files_to_conver.items():
    # print(f'{name_tag}, {info}')
    structura_base.add_model(name_tag,info["file"])  
    structura_base.set_model_offset(name_tag,info["offset"]) #设置偏移量
# 生成记录文件

# structura_base.generate_nametag_file()
# 把结构文件一起塞包里，但copy被我注释掉了
structura_base.generate_with_nametags()
structura_base.compile_pack()
# print(structura_base.compile_pack())
# print(structura_base.make_nametag_block_lists())

