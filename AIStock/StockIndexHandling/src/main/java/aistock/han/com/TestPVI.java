package aistock.han.com;

import java.util.ArrayList;
import java.util.List;

class PVIIndex {
    public String date;
    public double close;
    public double volume;
    public double pvi_value;
    public PVIIndex(String date, double close, double volunme) {
        this.date = date;
        this.close = close;
        this.volume = volunme;
        this.pvi_value = 1000.0;
    }
}
public class TestPVI {
    private List<PVIIndex> indexList;
    public TestPVI() {
        indexList = new ArrayList<PVIIndex>();
    }
    public void pvi() {
        makeSample();
        for(int i=1; i<indexList.size(); i++){
            if(indexList.get(i).volume > indexList.get(i-1).volume){
                PVIIndex temp = indexList.get(i);
                temp.pvi_value = indexList.get(i-1).pvi_value +
                        temp.pvi_value*((indexList.get(i).close - indexList.get(i-1).close)/indexList.get(i-1).close);
                indexList.set(i, temp);
            }else  {
                PVIIndex temp = indexList.get(i);
                temp.pvi_value = indexList.get(i-1).pvi_value + 0;
                indexList.set(i, temp);
            }
        }
        print();
    }
    public void print() {
        for(PVIIndex index : indexList){
            System.out.println(index.date+"\t"+index.close+"\t"+index.volume+"\t"+index.pvi_value);
        }
    }
    public void makeSample() {
        indexList.add(new PVIIndex("2005-11-01",81.59,5653100.00));
        indexList.add(new PVIIndex("2005-11-02",81.06,6447400.00));
        indexList.add(new PVIIndex("2005-11-03",82.87,7690900.00));
        indexList.add(new PVIIndex("2005-11-04",83.00,3831400.00));
        indexList.add(new PVIIndex("2005-11-07",83.61,4455100.00));
        indexList.add(new PVIIndex("2005-11-08",83.15,3798000.00));
        indexList.add(new PVIIndex("2005-11-09",82.84,3936200.00));
        indexList.add(new PVIIndex("2005-11-10",83.99,4732000.00));
        indexList.add(new PVIIndex("2005-11-11",84.55,4841300.00));
        indexList.add(new PVIIndex("2005-11-14",84.36,3915300.00));
        indexList.add(new PVIIndex("2005-11-15",85.53,6830800.00));
        indexList.add(new PVIIndex("2005-11-16",86.54,6694100.00));
        indexList.add(new PVIIndex("2005-11-17",86.89,5293600.00));
        indexList.add(new PVIIndex("2005-11-18",87.77,7985800.00));
        indexList.add(new PVIIndex("2005-11-21",87.29,4807900.00));
    }
}
