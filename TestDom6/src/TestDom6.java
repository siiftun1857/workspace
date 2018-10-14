import java.io.File;
import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
//import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

/**
 * @author siiftun1857
 *
 */
public class TestDom6 {
	
	final static String[] Datas = {"StringArray","String","Single","Boolean","Vector3","Color","MKey","MMenu","MToggle","MSlider","MLimits","MColourSlider",};
	
	static void getData(Element element)
	{
		for (int j = 0; j < Datas.length; ++j)
		{
			NodeList typedata = element.getElementsByTagName(Datas[j]);
			for (int k = 0; k < typedata.getLength(); ++k)
			{
				Element thisdata = (Element) typedata.item(k);
				System.out.println("");
				System.out.println("Data type:"+Datas[j]);
				System.out.println("key:"+thisdata.getAttributes().getNamedItem("key").getNodeValue());
				if(Datas[j] == "Vector3")
				{
					System.out.println("Value:");
					System.out.println("X:"+thisdata.getElementsByTagName("X").item(0).getFirstChild().getNodeValue());
					System.out.println("Y:"+thisdata.getElementsByTagName("Y").item(0).getFirstChild().getNodeValue());
					System.out.println("Z:"+thisdata.getElementsByTagName("Z").item(0).getFirstChild().getNodeValue());
				}
				else if(Datas[j] == "Color"||Datas[j] == "MColourSlider")
				{
					System.out.println("Value:");
					System.out.println("R:"+thisdata.getElementsByTagName("R").item(0).getFirstChild().getNodeValue());
					System.out.println("G:"+thisdata.getElementsByTagName("G").item(0).getFirstChild().getNodeValue());
					System.out.println("B:"+thisdata.getElementsByTagName("B").item(0).getFirstChild().getNodeValue());
				}
				else
				{
					System.out.println("Value:"+thisdata.getFirstChild().getNodeValue());
				}
			}
		}
	}
	
	/**
	 * @param args
	 * 
	 */
	public static void main(String[] args) {
		try {
			File file = new File("steam-cannon.xml");
			DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();	// step 1:���DOM����������:�����������Ǵ�������Ľ�����
			DocumentBuilder db = dbf.newDocumentBuilder();						// step 2����þ����dom������
			Document document = db.parse(file);			// step 3:����һ��xml�ĵ������Document���󣨸��ڵ㣩
			
			final Element MachineElement		=  (Element) document.getElementsByTagName("Machine").item(0);
			final Element GlobalElement			=  (Element) document.getElementsByTagName("Global").item(0);
			final NodeList BlockList			=( (Element) document.getElementsByTagName("Blocks").item(0) ).getElementsByTagName("Block");
			final NodeList DataList				=  document.getElementsByTagName("Data");
			
			final Element GlobalPosition		= (Element) GlobalElement.getElementsByTagName("Position").item(0);
			final Element GlobalRotation 		= (Element) GlobalElement.getElementsByTagName("Rotation").item(0);
			
			System.out.println("Machine:");
			System.out.println("version:"+MachineElement.getAttributes().getNamedItem("version").getNodeValue());
			if(MachineElement.getAttributes().getNamedItem("bsgVersion") != null)
				System.out.println("bsgVersion:"+MachineElement.getAttributes().getNamedItem("bsgVersion").getNodeValue());
			else
				System.out.println("bsgVersion not found");
			System.out.println("name:"+MachineElement.getAttributes().getNamedItem("name").getNodeValue());
			System.out.println("----------------------");
			System.out.println("Global Position:");
			System.out.println("x:"+GlobalPosition.getAttributes().getNamedItem("x").getNodeValue());
			System.out.println("y:"+GlobalPosition.getAttributes().getNamedItem("y").getNodeValue());
			System.out.println("z:"+GlobalPosition.getAttributes().getNamedItem("z").getNodeValue());
			System.out.println("----------------------");
			System.out.println("Global Rotation:");
			System.out.println("x:"+GlobalRotation.getAttributes().getNamedItem("x").getNodeValue());
			System.out.println("y:"+GlobalRotation.getAttributes().getNamedItem("y").getNodeValue());
			System.out.println("z:"+GlobalRotation.getAttributes().getNamedItem("z").getNodeValue());
			System.out.println("w:"+GlobalRotation.getAttributes().getNamedItem("w").getNodeValue());
			System.out.println("----------------------");
			
			System.out.println("Data:");
			getData((Element) DataList.item(0));
			System.out.println("----------------------");
			System.out.println("Blocks:"+BlockList.getLength());
			// ����ÿһ���ڵ�
			for (int i = 0; i < BlockList.getLength(); ++i)
			{
				System.out.println("----------------------");
				Element elementblock = (Element) BlockList.item(i);
				Element elementdata = (Element) elementblock.getElementsByTagName("Data").item(0);

/*				// ��ȡ��Ԫ�أ���Ԫ��titleֻ��һ���ڵ㣬֮��ͨ��getNodeValue������ȡ�ڵ��ֵ
//				String content0 = element.getElementsByTagName("title").item(0).getNodeValue();
//				System.out.println(content0);// �˴���ӡ��Ϊnull ��Ϊ�ڵ�getNodeValue��ֵ��ԶΪnull
				// �������������getFirstChild()
				content = element.getElementsByTagName("title").item(0)
						.getFirstChild().getNodeValue();
				System.out.println("title: " + content);
*/
				
				System.out.println("guid:"+elementblock.getAttributes().getNamedItem("guid").getNodeValue());
				System.out.println("id:"+elementblock.getAttributes().getNamedItem("guid").getNodeValue());
				if(((Element) elementblock.getElementsByTagName("Settings").item(0)) != null)
				{
					NodeList skinlist = ((Element) elementblock.getElementsByTagName("Settings").item(0)).getElementsByTagName("Skin");
					for (int k = 0; k < skinlist.getLength(); ++k)
					{
						Element thisskin = (Element) skinlist.item(k);
						System.out.println("");
						System.out.println("Skin:");
						System.out.println("name:"+thisskin.getAttributes().getNamedItem("name").getNodeValue());
						System.out.println("id:"+thisskin.getAttributes().getNamedItem("id").getNodeValue());
					}
				}
				
				getData(elementdata);
			}
			
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (SAXException e) {
			e.printStackTrace();
		} catch (NullPointerException e) {
			e.printStackTrace();
		}
	}

}
