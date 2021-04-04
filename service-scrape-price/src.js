const phantom = require('phantom');
const express = require('express');

const app = express()
const PORT = 4000

app.get('/', async (req, res) => {
    url = req.query.url
    let start = Date.now()
    const price = await scrapePrice(url);
    res.send("Price: " + price + " | scraped in " + (Date.now() - start) / 1000 + " seconds")
})

app.listen(PORT, console.log("listenting on port: " + PORT));


//-----------------------------------------------------------------
const urlExample = "https://www.amazon.it/gp/product/B07NTV64J2/ref=ppx_yo_dt_b_asin_image_o00_s00?ie=UTF8&psc=1"

async function scrapePrice(url) {
    ////phantom part/////
    const instance = await phantom.create();
    const page = await instance.createPage();
    await page.on("onResourceRequested", function (requestData) {
        console.info('Requesting', requestData.url)
    });
    const status = await page.open(url);
    const content = await page.property('content');
    await instance.exit();

    ////scraping part/////
    data = content
    target = '<span id="price_inside_buybox" class="a-size-medium a-color-price">'
    indexTarget = data.indexOf(target)
    price = (data.substring(indexTarget + target.length)).substring(0, data.substring(indexTarget + target.length).indexOf('&')).replace(/\s/g, "") //arriving to the first number of the price
    return price
};



