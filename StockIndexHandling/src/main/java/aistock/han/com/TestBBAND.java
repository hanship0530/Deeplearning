package aistock.han.com;

import java.util.ArrayList;
import java.util.List;

class BBANDIndex {
    public String date;
    public double close;
    public double bband_lower;
    public double bband_middle;
    public double bband_upper;

    public BBANDIndex(String date, double close) {
        this.date = date;
        this.close = close;
        this.bband_lower = 0;
        this.bband_middle = 0;
        this.bband_upper = 0;
    }
}

public class TestBBAND {
    private List<BBANDIndex> indexList;
    public TestBBAND() {
        indexList = new ArrayList<BBANDIndex>();
    }
    public void makeSample() {
        indexList.add(new BBANDIndex("2005-11-01",81.59));
        indexList.add(new BBANDIndex("2005-11-02",81.06));
        indexList.add(new BBANDIndex("2005-11-03",82.87));
        indexList.add(new BBANDIndex("2005-11-04",83.00));
        indexList.add(new BBANDIndex("2005-11-07",83.61));
        indexList.add(new BBANDIndex("2005-11-08",83.15));
        indexList.add(new BBANDIndex("2005-11-09",82.84));
        indexList.add(new BBANDIndex("2005-11-10",83.99));
        indexList.add(new BBANDIndex("2005-11-11",84.55));
        indexList.add(new BBANDIndex("2005-11-14",84.36));
        indexList.add(new BBANDIndex("2005-11-15",85.53));
        indexList.add(new BBANDIndex("2005-11-16",86.54));
        indexList.add(new BBANDIndex("2005-11-17",86.89));
        indexList.add(new BBANDIndex("2005-11-18",87.77));
        indexList.add(new BBANDIndex("2005-11-21",87.29));
    }
}

