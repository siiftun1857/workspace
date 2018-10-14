import java.io.File;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
@SuppressWarnings("unused")
/**
 * http://www.cnblogs.com/mengdd/archive/2013/06/01/3113291.html
 */
public class TestDom5
{
    public static void main(String[] args) throws Exception
    {
        // step 1:获得DOM解析器工厂
        // 工厂的作用是创建具体的解析器
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

        // step 2：获得具体的dom解析器
        DocumentBuilder db = dbf.newDocumentBuilder();

        // step 3:解析一个xml文档，获得Document对象（根节点）
        // 此文档放在项目目录下即可
        Document document = db.parse(new File("books.xml"));

        // 根据标签名访问节点
        NodeList list = document.getElementsByTagName("book");
        System.out.println("list length: " + list.getLength());

        // 遍历每一个节点
        for (int i = 0; i < list.getLength(); ++i)
        {
            System.out.println("----------------------");
            // 获得元素，将节点强制转换为元素
            Element element = (Element) list.item(i);
            // 此时element就是一个具体的元素

            // 获取子元素：子元素title只有一个节点，之后通过getNodeValue方法获取节点的值
			String content0 = element.getElementsByTagName("title").item(0)
                    .getNodeValue();

//			System.out.println(content0);// 此处打印出为null
            // 因为节点getNodeValue的值永远为null

            // 解决方法：加上getFirstChild()
            String content = element.getElementsByTagName("title").item(0)
                    .getFirstChild().getNodeValue();
            System.out.println("title: " + content);// 此处打印出书名

            // 后面类似处理即可：
            content = element.getElementsByTagName("author").item(0)
                    .getFirstChild().getNodeValue();
            System.out.println("author: " + content);
            content = element.getElementsByTagName("year").item(0)
                    .getFirstChild().getNodeValue();
            System.out.println("year: " + content);
            content = element.getElementsByTagName("price").item(0)
                    .getFirstChild().getNodeValue();
            System.out.println("price: " + content);
        }
    }

}