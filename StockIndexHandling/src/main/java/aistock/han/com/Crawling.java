package aistock.han.com;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;


import java.net.MalformedURLException;
import java.util.HashMap;
import java.util.Map;
import org.ektorp.CouchDbConnector;
import org.ektorp.CouchDbInstance;
import org.ektorp.http.HttpClient;
import org.ektorp.http.StdHttpClient;
import org.ektorp.impl.StdCouchDbInstance;

public class Crawling {
    public static void main(String[] args) throws IOException {
        HttpClient httpClient = new StdHttpClient.Builder()
                .url("http://localhost:5984")
                .build();

        CouchDbInstance dbInstance = new StdCouchDbInstance(httpClient);
        // if the second parameter is true, the database will be created if it
        // doesn't exists
        CouchDbConnector db = dbInstance.createConnector("aistock", false);

        String stockCode = "008700"+".KS";
        String from = "1530630000";
        String to = "1562166000";
        String userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.33 (KHTML, like Gecko) Chrome/27.0.1438.7 Safari/537.33";
        String url = "https://finance.yahoo.com/quote/"+stockCode+"/history?period1="+from+"&period2="+to+"&interval=1d&filter=history&frequency=1d";
        String[] indice = new String[]{"_id", "Open", "High", "Low", "Close", "Adj Close", "Volume"};
        Document doc = Jsoup.connect(url)
                .userAgent(userAgent)
                .timeout(10*1000).get();
        String title = doc.title();
        System.out.println("title: "+title);
        Elements tr_list = doc.body().select("tbody").first().select("tr");
        System.out.println("Date\tOpen\tHigh\tLow\tClose\tAdj Close\tVolume");
        for(Element tr : tr_list) {
            Elements td_list = tr.select("td");
            Map<String, Object> map = new HashMap<String, Object>();
            int index=0;
            for(Element td : td_list){
                System.out.print(td.text()+"\t");
                map.put(indice[index++], td.text());
            }
            db.create(map);
            System.out.println("");
        }
    }
}

