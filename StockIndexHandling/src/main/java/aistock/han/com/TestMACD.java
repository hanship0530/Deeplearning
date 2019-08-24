package aistock.han.com;

class MACDIndex {
    String date;
    double close;
    double ema;
    double macd;
    double macd_signal;
    double macd_hist;

    public MACDIndex(String date, double close) {
        this.date = date;
        this.close = close;
        this.ema = 0;
        this.macd = 0;
        this.macd_signal = 0;
        this.macd_hist = 0;
    }
}
public class TestMACD {
    private MACDIndex[] indexList;
    public TestMACD() {
        indexList = new MACDIndex[15];
    }
    public void macd(int short_period, int long_period, int singal_period) {
        // a = 2/(n+1)
        // ema(t) = (1-a)*ema(t-1) + a*close(t)
        makeSample();
        double[] shortList = new double[15];
        double[] longList = new double[15];
        double short_a = 2.0/(short_period+1);
        double long_a = 2.0/(long_period+1);
        double singal_a = 2.0/(singal_period+1);
        shortList[0] = indexList[0].close;
        longList[0] = indexList[0].close;
        indexList[0].macd = shortList[0] - longList[0];
        indexList[0].macd_signal = indexList[0].macd;
        //indexList[0].macd_signal = (1.0-singal_a)*indexList[0].macd + singal_a*indexList[0].macd;
        indexList[0].macd_hist = indexList[0].macd - indexList[0].macd_signal;
        for(int i=1; i < indexList.length; i++){
            shortList[i] = (1.0-short_a)*shortList[i-1] + short_a*indexList[i].close;
            longList[i] = (1.0-long_a)*longList[i-1] + long_a*indexList[i].close;
            indexList[i].macd = shortList[i] - longList[i];
            indexList[i].macd_signal = (1.0-singal_a)*indexList[i-1].macd_signal + singal_a*indexList[i].macd;
            indexList[i].macd_hist = indexList[i].macd - indexList[i].macd_signal;
        }
        print();
    }
    public void print(){
        for(MACDIndex index : indexList){
            System.out.println(index.date+"\t"+index.close+"\t"+index.macd+"\t"+index.macd_signal+"\t"+index.macd_hist);
        }
    }
    public void makeSample(){
        indexList[0] = new MACDIndex("2005-11-01",81.59);
        indexList[1] = new MACDIndex("2005-11-02",81.06);
        indexList[2] = new MACDIndex("2005-11-03",82.87);
        indexList[3] = new MACDIndex("2005-11-04",83.00);
        indexList[4] = new MACDIndex("2005-11-07",83.61);
        indexList[5] =new MACDIndex("2005-11-08",83.15);
        indexList[6] =new MACDIndex("2005-11-09",82.84);
        indexList[7] =new MACDIndex("2005-11-10",83.99);
        indexList[8] =new MACDIndex("2005-11-11",84.55);
        indexList[9] =new MACDIndex("2005-11-14",84.36);
        indexList[10] =new MACDIndex("2005-11-15",85.53);
        indexList[11] =new MACDIndex("2005-11-16",86.54);
        indexList[12] =new MACDIndex("2005-11-17",86.89);
        indexList[13] =new MACDIndex("2005-11-18",87.77);
        indexList[14] =new MACDIndex("2005-11-21",87.29);
    }
}
