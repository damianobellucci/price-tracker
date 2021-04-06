

(async () => {
    try {

        const initialization = await initPhantom()

        const express = require('express')

        const app = express();

        var cors = require('cors')
        app.use(cors())

        const PORT = 4002;

        var counter = 0;

        app.get('/', async (req, res) => {
            url = req.query.url
            const call = await scrapePrice(url, initialization);
            counter = counter + 1;
            let response = { price: call.price, time: call.time, counter: counter }
            res.send(response)
        })

        app.get("/test", (req, res) => {
            res.send("test ok")
        })

        app.listen(PORT, console.log("listenting on port: " + PORT));

    } catch (e) {
        console.log(e)
    }
})()



async function scrapePrice(url, page) {
    let start = Date.now()
    const status = await page.open(url);
    const content = await page.property('content');
    ////scraping part/////
    data = content
    target = '<span id="price_inside_buybox" class="a-size-medium a-color-price">'
    indexTarget = data.indexOf(target)
    price = (data.substring(indexTarget + target.length)).substring(0, data.substring(indexTarget + target.length).indexOf('&')).replace(/\s/g, "") //arriving to the first number of the price
    let end = Date.now()
    return { price: price, time: (end - start) / 1000 }
};

async function initPhantom() {
    const instance = await require('phantom').create();
    const page = await instance.createPage();
    return page
}