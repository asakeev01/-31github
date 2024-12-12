def version_compare( version1, version2 ) :
  first = version1.split(".")
  second = version2.split(".")
  while len(first) < len(second):
      first.append("0")
  while len(second) < len(first):
      second.append("0")
  for i in range(len(first)):
      if int(first[i]) > int(second[i]):
          return 1
      elif int(first[i]) < int(second[i]):
          return -1
  return 0

print(version_compare("2", "2.0.0.0"))
