package aistock.han.com;

import java.util.ArrayList;
import java.util.List;

class OBVIndex {
    String date;
    double close;
    double volume;
    double obv;
    public OBVIndex(String date, double close, double volume){
        this.date = date;
        this.close = close;
        this.volume = volume;
        this.obv = 0;
    }
    public void setObv(double obv) {
        this.obv = obv;
    }
}
public class TestOBV {
    private List<OBVIndex> indexList;
    public TestOBV() {
        indexList = new ArrayList<OBVIndex>();
    }
    public void obv() {
        makeSample();
        for(int i=1; i<indexList.size(); i++){
            if(indexList.get(i).close > indexList.get(i-1).close ){
                //indexList.get(i).setObv(indexList.get(i-1).obv + indexList.get(i).volume);
                OBVIndex temp = indexList.get(i);
                temp.setObv(indexList.get(i-1).obv + indexList.get(i).volume);
                indexList.set(i, temp);
            }
            else if(indexList.get(i).close <indexList.get(i-1).close ){
                //indexList.get(i).setObv(indexList.get(i-1).obv - indexList.get(i).volume);
                OBVIndex temp = indexList.get(i);
                temp.setObv(indexList.get(i-1).obv - indexList.get(i).volume);
                indexList.set(i, temp);
            }
            else {
                //indexList.get(i).setObv(0);
                OBVIndex temp = indexList.get(i);
                temp.setObv(0.0);
                indexList.set(i, temp);
            }
        }
        print();
    }
    public void print() {
        for(OBVIndex index : indexList){
            System.out.println(index.date+"\t"+index.close+"\t"+index.volume+"\t"+index.obv);
        }
    }
    public void makeSample() {
        indexList.add(new OBVIndex("2005-11-01",81.59,5653100.00));
        indexList.add(new OBVIndex("2005-11-02",81.06,6447400.00));
        indexList.add(new OBVIndex("2005-11-03",82.87,7690900.00));
        indexList.add(new OBVIndex("2005-11-04",83.00,3831400.00));
        indexList.add(new OBVIndex("2005-11-07",83.61,4455100.00));
        indexList.add(new OBVIndex("2005-11-08",83.15,3798000.00));
        indexList.add(new OBVIndex("2005-11-09",82.84,3936200.00));
        indexList.add(new OBVIndex("2005-11-10",83.99,4732000.00));
        indexList.add(new OBVIndex("2005-11-11",84.55,4841300.00));
        indexList.add(new OBVIndex("2005-11-14",84.36,3915300.00));
        indexList.add(new OBVIndex("2005-11-15",85.53,6830800.00));
        indexList.add(new OBVIndex("2005-11-16",86.54,6694100.00));
        indexList.add(new OBVIndex("2005-11-17",86.89,5293600.00));
        indexList.add(new OBVIndex("2005-11-18",87.77,7985800.00));
        indexList.add(new OBVIndex("2005-11-21",87.29,4807900.00));
    }
}
