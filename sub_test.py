import re

dict_s = {}
d = "<Customer  abModelFlag=\"A\" addr=\"SH\" adjLmtImportCustList=\"-999999\" advWarningImportCusList=\"-999999\" alopCred=\"-9999999\" alsM12Caoff=\"-999999\" alsM12Caon=\"-999999\"><PbocReport  creditScore=\"-9999999\" eduDegree=\"-999999\" eduLevel=\"-9999999\" gender=\"1\" mobile=\"13312345678\"></PbocReport><CardInfo  c_id=\"-999999\" currency=\"CNY\"><CardInfo  c_id=\"-999999\" cardType=\"1\"></CardInfo>"
s = "<Customer  abModelFlag=\"A\" addr=\"SH\" adjLmtImportCustList=\"-999999\" advWarningImportCusList=\"-999999\" alopCred=\"-9999999\" alsM12Caoff=\"-999999\" alsM12Caon=\"-999999\"><Customer1  abModelFlag=\"A\" addr=\"SF\" adjLmtImportCustList=\"-999988\" advWarningImportCusList=\"-999999\" alopCred=\"-9999977\" alsM12Caoff=\"-999999\" alsM12Caon=\"-999999\"><PbocReport  creditScore=\"-9999999\" eduDegree=\"-999999\" eduLevel=\"-9999999\" gender=\"1\" mobile=\"13312345678\"></PbocReport><CardInfo1  c_id=\"-999999\" currency=\"CNY\"><CardInfo  c_id=\"-999999\" cardType=\"1\"></CardInfo>"

s1=[]
s2=[]
dict_rap={}
group = re.findall('<(\w+)(.*?)>',s)
print(len(group))
# print(group[0])
for nd in range(0,len(group)):
    dic1 = {group[nd][0]:group[nd][1] for i in group[nd]}
    for k,v in dic1.items():
        dict_rap[k]=v
print(dict_rap)
dict_new ={}
for k,v in dict_rap.items():
    temp_list = v.split()
    l= dict(i.split("=")for i in temp_list)
    for k,v in l.items() :
        dict_new[k]=v
    dict_rap[k]=dict_new


print(dict_new)
print(dict_rap)
    #dic2 = {group[1][0]:group[1][1] for i in group[1]}

# list = []
# for k,v in dic1.items():
#     a = v.split()
#     if not None:
#         s.extend(a)
#
# for k,v in dic2.items():
#     a = v.split()
#     if not None:
#         s2.extend(a)
# l =dict(i.split("=") for i in s)
# l2 =dict(i.split("=") for i in s2)
#
# for i in l.keys():
#     for j in l2.keys():
#         if(i==j) and l[i] != l2[j]:
#             print(f'<{i}>标签 : 新值: {l[i]}  旧值: {l2[j]}')
#
#
# print(l)
# print(l2)

def go_compare(new,old):
    ...

def compare2diffrent(str:str,str2:str):
    # 第一步截取到固定位置,截取到固定位置的方法  def sub_xml :return str,str1
    # 第二步正则匹配转为字典，逐步遍历比较value   def go_compare : return str

    ...





