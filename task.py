profile = {
    "name":"ram",
    "gender":"male",
    "educations":[
        {"college":"abc college", "level":"+2"},
        {"college":"xyz college", "level":"bachelor"},
    ],
    "addresses":[
        {
            "temporary": {
                "ward":"1",
                "city":"kathmandu"
            },
            "permanent": {
                "ward":"2",
                "city":"kavre"

            }
        }
    ]

}


#print(f"name:{profile.get('name')}")
#print(f"gender:{profile.get('gender')}")

#educations = profile.get('educations')
#for education in educations:
#    print(f"college:{education.get('college')} and level:{education.get('level')}")

#addresses = profile.get('addresses')
#for address in addresses:
#    print(address.get('temporary').get('city'))
    #permanent = address.get('permanent')
    #print(f"ward:{temporary.get('ward')} and city:{temporary.get('city')}")
    #print(f"ward:{permanent.get('ward')} and city:{permanent.get('city')}")
addresses = profile.get('addresses')
for address in addresses:
    for key, val in address.items():
        print(key, val.get('ward'))