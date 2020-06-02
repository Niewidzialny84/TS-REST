import requests
import time

polished_andesite=json={
    "group": "",
    "input": {
      "amount": 4,
      "item0": [
        "ANDESITE"
      ],
      "item1": [
        "ANDESITE"
      ],
      "item2": [
        "ANDESITE"
      ],
      "item3": [
        "ANDESITE"
      ],
      "sign0": "a",
      "sign1": "b",
      "sign2": "c",
      "sign3": "d"
    },
    "output": {
      "==": "org.bukkit.inventory.ItemStack",
      "amount": 4,
      "type": "POLISHED_ANDESITE",
      "v": 1976
    },
    "shape": [
      "ab",
      "cd"
    ],
    "type": "ShapedRecipe"
}


serviceAddress="http://192.168.1.100:5000/"

print("Recipe GET")
time.sleep(0.5)
myget = requests.get(serviceAddress+'/recipe/polished_andesite')
print(myget.text)

print("Recipe GET input amount")
time.sleep(0.5)
myget = requests.get(serviceAddress+'/recipe/polished_andesite/input-amount')
print(myget.text)

print("Recipe GET output amount")
time.sleep(0.5)
myget = requests.get(serviceAddress+'/recipe/polished_andesite/output-amount')
print(myget.text)

print("Recipe POST output amount")
time.sleep(0.5)
mypost = requests.post(serviceAddress+'/recipe/polished_andesite/output-amount')
print(mypost.text)

print("Recipe DELETE recipe polished_andesite")
time.sleep(0.5)
mydelete= requests.delete(serviceAddress+'/recipe/polished_andesite')
print(mydelete.text)

print("Recipe PUT polished_andesite")
time.sleep(0.5)
myput = requests.put(serviceAddress+'/recipe/polished_andesite', json=polished_andesite)
print(myput.text)
