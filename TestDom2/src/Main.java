import com.test.xml.XmlImpl;;
/** 
 * http://www.cnblogs.com/wangchenyang/archive/2011/08/23/2150530.html
 */
public class Main {
 
    public static void main(String args[]){
        String str="grade.xml";
        XmlImpl dd=new XmlImpl();
        dd.init();
        dd.createXml(str);    //¥¥Ω®xml
        dd.parserXml(str);    //∂¡»°xml
    }
}