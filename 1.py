from string import maketrans, ascii_lowercase;
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj."""
#table = string.maketrans(
#string.ascii_lowercase,
#string.ascii_lowercase[2:]+string.ascii_lowercase[:2])

tran = ascii_lowercase[2:] + ascii_lowercase[:2]
org = ascii_lowercase
rot2 = maketrans(org,tran)

print text.translate(rot2)
