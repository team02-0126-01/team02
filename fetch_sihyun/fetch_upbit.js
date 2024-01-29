let coinData = [];
const fetchData = (coinList) => {
    coinList.forEach((coin) =>
        fetch(`https://api.upbit.com/v1/ticker?markets=${coin}`)
            .then((response) => response.json())
            .then((json) => getCoinData(json[0]))
            .catch((err) => console.error(err))
    );

    const getCoinData = ({ ...coin }) => {
        const symbol = coin.market.slice(4);
        const change = (coin.change === "FALL" ? "-" : coin.change === "RISE" ? "+" : "")
        const tradePrice = coin.trade_price.toLocaleString();
        const changePrice = change + coin.change_price.toLocaleString();
        const changeRate = change + (Number(coin.change_rate) * 100).toFixed(2);
        const coinInfo = {
            symbol: symbol,
            tradePrice: tradePrice,
            changePrice: changePrice,
            changeRate: changeRate,
        };
        coinData = [...coinData, coinInfo]
        console.log(coinData)
    };

};

const coinList = [
    "KRW-BTC",
    "KRW-ETH",
    "KRW-SOL",
    "KRW-AVAX",
    "KRW-STX",
    "KRW-DOGE",
];
fetchData(coinList);
