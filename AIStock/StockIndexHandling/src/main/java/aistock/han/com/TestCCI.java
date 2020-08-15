package aistock.han.com;

import java.util.ArrayList;
import java.util.List;
import java.lang.Math;
class Index {
    String date;
    double high;
    double low;
    double close;
    double typprice;
    public Index(String date, double high, double low, double close){
        this.date = date;
        this.high = high;
        this.low = low;
        this.close = close;
        this.typprice = (high + low + close)/3;

    }
}

public class TestCCI {
    private List<Index> indexList;
    public TestCCI() {
        indexList = new ArrayList<Index>();
    }
    public void sma(int period) {

    }
    public void cci(int period){
        makeSample();
        for(int i=period-1; i<indexList.size(); i++){
            double atyppric=0;
            double mdt=0;
            double cci;
            for(int j=i-period+1; j<=i; j++){
                atyppric += indexList.get(j).typprice;
            }
            atyppric = atyppric / period;
            for(int j=i-period+1; j<=i; j++){
                mdt += Math.abs(indexList.get(j).typprice - atyppric);
            }
            mdt = mdt / period;
            cci = (indexList.get(i).typprice - atyppric)/(0.015*mdt);
            System.out.println(indexList.get(i).date+"\t"+indexList.get(i).typprice+"\t"+atyppric+"\t"+mdt+"\t"+cci);
        }
    }
    public void makeSample() {
        indexList.add(new Index("2005-11-01",82.15,81.29,81.59));
        indexList.add(new Index("2005-11-02",82.89,80.64,81.06));
        indexList.add(new Index("2005-11-03",83.03,81.31,82.87));
        indexList.add(new Index("2005-11-04",83.30,82.65,83.00));
        indexList.add(new Index("2005-11-07",83.85,83.07,83.61));
        indexList.add(new Index("2005-11-08",83.90,83.11,83.15));
        indexList.add(new Index("2005-11-09",83.33,82.49,82.84));
        indexList.add(new Index("2005-11-10",84.30,82.30,83.99));
        indexList.add(new Index("2005-11-11",84.84,84.15,84.55));
        indexList.add(new Index("2005-11-14",85.00,84.11,84.36));
        indexList.add(new Index("2005-11-15",85.90,84.03,85.53));
        indexList.add(new Index("2005-11-16",86.58,85.39,86.54));
        indexList.add(new Index("2005-11-17",86.98,85.76,86.89));
        indexList.add(new Index("2005-11-18",88.00,87.17,87.77));
        indexList.add(new Index("2005-11-21",87.87,87.01,87.29));
    }
}
