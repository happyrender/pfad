import requests
url = "https://www.hko.gov.hk/tide/CLKtextPH2025_uc.htm"
from bs4 import BeautifulSoup as bs
import numpy as np
import matplotlib.pyplot as plt


response=requests.get(url)
content = response.text
soup = bs(content,"html.parser")
weatherData = []
renders = soup.findAll("td")
for render in renders:
    renderValue = render.string

    if renderValue !=None and renderValue[0]==" ":
        weatherData.append(float(renderValue.strip()))
       


weatherData = weatherData[:31*24]
render = np.array(weatherData).reshape(31,24)


print(render[30])



t = np.arange(0, 24)
s = render[30]

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (h)', ylabel='tide height',
       title='tide height in Jan 31st')
ax.grid()

fig.savefig("test.png")
plt.show()


