package aistock.han.com;
import org.ektorp.CouchDbConnector;
import org.ektorp.CouchDbInstance;
import org.ektorp.http.HttpClient;
import org.ektorp.http.StdHttpClient;
import org.ektorp.impl.StdCouchDbInstance;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

public class Crawling {
    public static void main(String[] args) throws IOException {
        String stockCode = "008700"+".KS";
        String from = "1530630000";
        String to = "1562166000";
        String userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.33 (KHTML, like Gecko) Chrome/27.0.1438.7 Safari/537.33";
        String url = "https://finance.yahoo.com/quote/"+stockCode+"/history?period1="+from+"&period2="+to+"&interval=1d&filter=history&frequency=1d";
        Document doc = Jsoup.connect(url)
                .userAgent(userAgent)
                .timeout(10*1000).get();
        String title = doc.title();
        System.out.println("title: "+title);
        Elements tr_list = doc.body().select("tbody").first().select("tr");
        System.out.println("Data\tOpen\tHigh\tLow\tClose\tAdj Close\tVolume");
        for(Element tr : tr_list) {
            Elements td_list = tr.select("td");
            for(Element td : td_list){
                System.out.print(td.text()+"\t");
            }
            System.out.println("");
        }
        HttpClient httpClient = new StdHttpClient.Builder()
                .url("http://192.168.99.100:5984/")
                .username("mapUser")
                .password("myCouchDBSecret")
                .build();
        protected static CouchDbInstance dbi;
        dbi = new StdCouchDbInstance(httpClient);
        CouchDbConnector dbc = dbi.createConnector(CouchInjector.DB_NAME, false);

        repo = new MapRepository();
        repo.db = dbc;
        repo.postConstruct();
        debugWriter = repo.sites.mapper.writerWithDefaultPrettyPrinter();
    }
}
