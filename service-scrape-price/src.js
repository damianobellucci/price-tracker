const phantom = require('phantom');

(async function () {
    ////phantom part/////
    const instance = await phantom.create();
    const page = await instance.createPage();
    await page.on("onResourceRequested", function (requestData) {
        console.info('Requesting', requestData.url)
    });
    let url = "https://www.amazon.it/gp/product/B07NTV64J2/ref=ppx_yo_dt_b_asin_image_o00_s00?ie=UTF8&psc=1"
    const status = await page.open(url);
    const content = await page.property('content');
    await instance.exit();

    ////scraping part/////
    data = content
    target = '<span id="price_inside_buybox" class="a-size-medium a-color-price">'
    indexTarget = data.indexOf(target)
    price = (data.substring(indexTarget + target.length)).substring(0, data.substring(indexTarget + target.length).indexOf('&')).replace(/\s/g, "") //arriving to the first number of the price
    console.log(price)
}());



