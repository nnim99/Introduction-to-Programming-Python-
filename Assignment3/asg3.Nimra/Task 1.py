import NMStringProcessor
def main():
	string01 = "adhuashduib"
	string02 = 1256432
	string03 = "edhui327"
	string04 = "SJHDSKFBJJKG"
	string05 = "hello world"
	string06 = "My name is Nimra"
	string07 = "+++jskdjjd jjsh skj++++"
	string08 = "     "
	print("String01:",string01)
	print("String02:",string02)
	print("String03:",string03)
	print("String04:",string04)
	print("String05:",string05)
	print("String06:",string06)
	print("String07:",string07)
	print("String08:",string08)
	print("Capitalize")
	print(NMStringProcessor.capitalize(string05))
	print("Title")
	print(NMStringProcessor.title(string05))
	print("islower")
	print(NMStringProcessor.islower(string03))
	print("islower")
	print(NMStringProcessor.islower(string06))
	print("isupper")
	print(NMStringProcessor.isupper(string06))
	print("isupper")
	print(NMStringProcessor.isupper(string04))
	print("isdigit")
	print(NMStringProcessor.isdigit(string02))
	print("isdigit")
	print(NMStringProcessor.isdigit(string03))
	print("endsWith")
	print(NMStringProcessor.endsWith(string01,"uib"))
	print("endsWith")
	print(NMStringProcessor.endsWith(string05,"uib"))
	print("startsWith")
	print(NMStringProcessor.startsWith(string05,"hell"))
	print("startsWith")
	print(NMStringProcessor.startsWith(string05,"hjaj"))
	print("lstrip")
	print(NMStringProcessor.lstrip(string07,"+"))
	print("rstrip")
	print(NMStringProcessor.rstrip(string07,"+"))
	print("strip")
	print(NMStringProcessor.strip(string07,"+"))
	print("replace")
	print(NMStringProcessor.replace(string05,"l","n"))
	print("replaceWithBounds")
	print(NMStringProcessor.replaceWithBounds(string05,"l","n",2,7))
	print("isspace")
	print(NMStringProcessor.isspace(string08))
	print("isalpha")
	print(NMStringProcessor.isspace(string04))
	print("swapcase")
	print(NMStringProcessor.swapcase(string06))
	print("lower")
	print(NMStringProcessor.lower(string06))
	print("upper")
	print(NMStringProcessor.upper(string06))
	print("length of string06")
	print(NMStringProcessor.length(string06))
	print("count l")
	print(NMStringProcessor.count(string05,"l"))
	print("countWithBounds l")
	print(NMStringProcessor.countWithBounds(string05,"l",2,7))
	print("reverse")
	print(NMStringProcessor.reverse(string06))
	print("find")
	print(NMStringProcessor.find(string05,"l"))
	print("rfind")
	print(NMStringProcessor.rfind(string05,"l"))
	print("findWithBounds")
	print(NMStringProcessor.findWithBounds(string05,"l",2,7))
	print("find")
	print(NMStringProcessor.find(string06,"l"))
	print("index")
	print(NMStringProcessor.index(string05,"l"))
	print("rindex")
	print(NMStringProcessor.rindex(string05,"l"))
	print("indexWithBounds")
	print(NMStringProcessor.indexWithBounds(string05,"l",2,7))
	print("index")
	print(NMStringProcessor.index(string06,"l"))
main()