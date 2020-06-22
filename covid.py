import requests,json,pyfiglet

response = requests.get('https://covid19.mohp.gov.np/covid/api/confirmedcases')
data = json.loads(response.content.decode())

golbaldata = data['global']
nepaldata = data['nepal']

text = pyfiglet.figlet_format('COVID19')
print(text)
print('-'*100)
print('\n')
print(f"   Global Postive     :    {golbaldata['positive']}")
print(f"   Global Death       :    {golbaldata['deaths']} ")
print(f"   Nepal Postive      :    {nepaldata['positive']}")
print(f"   Nepal Death        :    {nepaldata['deaths']} ")

print('\n')
print('-'*100)
