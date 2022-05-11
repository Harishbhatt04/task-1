dict1 = {
    "april_batch":{
        "student":{
            "name":"mike",
            "marks":{
                "python":80,
                "maths":70
                }
            }
        }
    }
print(dict1["april_batch"]["student"]["name"])

print(dict1["april_batch"]["student"]["marks"]["python"])

dict1["april_batch"]["student"]["name"]="Harish"
print(dict1)

dict1["april_batch"]["student"]["marks"].update({"AL":80,"DL":80})
print(dict1)




