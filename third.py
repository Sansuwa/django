#DICT

# a={}
# type(a)

# a ={"name":"ram","contact":"98765","address":"ktm"}
# a["name"] -helps to access values of given key .it raises keyerror when asked for key not available
# 'ram'

#CLEAR :empties the dict
# a.clear()

# #COPY :copies all values so that they wont be identical DATA are allocated differently in different memory address as different object is made
# a.copy()

# EXAMPLE:
#  >>> a
# {'name': 'ram', 'contact': '98765', 'address': 'ktm'}
# >>> b=a (saves obj in same mem address or makes same obj)
# >>> a
# {'name': 'ram', 'contact': '98765', 'address': 'ktm'}
# >>> id(a)
# 2151486634560
# >>> id(b)
# 2151486634560
# >>> c=a.copy()
# >>> c
# {'name': 'ram', 'contact': '98765', 'address': 'ktm'}
# >>> id(c)
# 2151486634944

#GET,SETDEFAULT

#GET
# >>> a
# {'name': 'ram', 'contact': '98765', 'address': 'ktm'}
# >>> a.get("name")
# 'ram'
# >>> a.get("gender") -doesnot raises error
# >>> a["gender"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'gender'
# >>> a.get("gender","Unknown") -key gender is not available
# 'Unknown'
# >>> a.get("name","Anon")
# 'ram'
# >>> print(a.get("gender"))
# None

# SETDEFAULT :returns the updated set of data if passes unmentioned key
# >>> a
# {'name': 'ram', 'contact': '98765', 'address': 'ktm'}
# >>> a.setdefault("name")
# 'ram'
# >>> a.setdefault("name","Anon")
# 'ram'
# >>> a.setdefault("gender","unknown")
# 'unknown'
# >>> a
# {'name': 'ram', 'contact': '98765', 'address': 'ktm', 'gender': 'unknown'}

#POP
# >>> a
# {'contact': '98765', 'address': 'ktm', 'gender': 'unknown'}
# >>> a.pop("contact")
# '98765'
# >>> a
# {'address': 'ktm', 'gender': 'unknown'}

#POPITEM  -pop item works on LIFO method so removes last added key and value
# >>> a.popitem()
# ('gender', 'unknown')

#UPGRADE -addups the passed key and value to the given dict
# >>> a
# {'address': 'ktm'}
# >>> a.update({"name":"ram","contact":"9846224","gender":"Female"})
# >>> a
# {'address': 'ktm', 'name': 'ram', 'contact': '9846224', 'gender': 'Female'}


#SOME IMPORTANT COMMANDS
# >>> a.keys()
# dict_keys(['address', 'name', 'contact', 'gender'])
# >>> a.values()
# dict_values(['ktm', 'ram', '9846224', 'Female'])
# >>> a.items()
# dict_items([('address', 'ktm'), ('name', 'ram'), ('contact', '9846224'), ('gender', 'Female')]) -values in tuples
