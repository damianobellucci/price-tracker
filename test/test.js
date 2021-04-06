urls = [
    'https://www.amazon.it/gp/product/B07NTV64J2/ref=ppx_yo_dt_b_asin_image_o00_s00?ie=UTF8&psc=1',
    'https://www.amazon.it/LG-27UL500-Monitor-FreeSync-Multitasking/dp/B07PVW7BMQ/ref=pd_bxgy_img_2/262-8805141-0189019?_encoding=UTF8&pd_rd_i=B07PVW7BMQ&pd_rd_r=7460bc9b-7c76-45cf-b633-a28d7fcdc0dd&pd_rd_w=NUBJw&pd_rd_wg=IeqdU&pf_rd_p=1a9790af-369b-4642-b8de-6cff93a1a290&pf_rd_r=Q6FTRC0344ZAF3AVNX62&psc=1&refRID=Q6FTRC0344ZAF3AVNX62'
];
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async function () {
    for (let i = 0; i < 100000; i++) {
        let start = Date.now()
        let response = await require('axios').get("http://localhost:4002?url=https://www.amazon.it/gp/product/B07NTV64J2/ref=ppx_yo_dt_b_asin_image_o00_s00?ie=UTF8&psc=1")
        console.log(response.data)
        await sleep(15000)
        console.log((Date.now() - start) / 1000)
    }
})()