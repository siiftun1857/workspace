package xidian.sl.dom;

import java.io.FileOutputStream;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.apache.crimson.tree.XmlDocument;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

/**
 * http://www.cnblogs.com/shenliang123/archive/2012/05/11/2495252.html
 */
public class DomDemo {
    /**
     * ����xml�ĵ�
     * */
    public static void queryXml(){
        try{
            //�õ�DOM�������Ĺ���ʵ��
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            //��DOM�����л��DOM������
            DocumentBuilder dbBuilder = dbFactory.newDocumentBuilder();
            //��Ҫ������xml�ĵ�����DOM������
            Document doc = dbBuilder.parse("school.xml");
            System.out.println("������ĵ���DomImplementation����  = "+ doc.getImplementation());
            //�õ��ĵ�����ΪStudent��Ԫ�صĽڵ��б�
            NodeList nList = doc.getElementsByTagName("Student");
            //�����ü��ϣ���ʾ����е�Ԫ�ؼ�����Ԫ�ص�����
            for(int i = 0; i< nList.getLength() ; i ++){
                Element node = (Element)nList.item(i);
                System.out.println("Name: "+ node.getElementsByTagName("Name").item(0).getFirstChild().getNodeValue());
                System.out.println("Num: "+ node.getElementsByTagName("Num").item(0).getFirstChild().getNodeValue());
                System.out.println("Classes: "+ node.getElementsByTagName("Classes").item(0).getFirstChild().getNodeValue());
                System.out.println("Address: "+ node.getElementsByTagName("Address").item(0).getFirstChild().getNodeValue());
                System.out.println("Tel: "+ node.getElementsByTagName("Tel").item(0).getFirstChild().getNodeValue());
            }
            
        }catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }
    /**
     * ���Ѵ��ڵ�xml�ļ��в���Ԫ��
     * */
    public static void insertXml(){
        Element school = null;
        Element student = null;
        Element name = null;
        Element num = null;
        Element classes = null;
        Element address = null;
        Element tel = null;
        try{
            //�õ�DOM�������Ĺ���ʵ��
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            //��DOM�����л��DOM������
            DocumentBuilder dbBuilder = dbFactory.newDocumentBuilder();
            //��Ҫ������xml�ĵ�����DOM������
            Document doc = dbBuilder.parse("school.xml");
            //�õ��ĵ�����ΪStudent��Ԫ�صĽڵ��б�
            NodeList nList = doc.getElementsByTagName("School");
            school = (Element)nList.item(0);
            //��������ΪStudent��Ԫ��
            student = doc.createElement("Student");
            //����Ԫ��Student������ֵΪ231
            student.setAttribute("examId", "23");
            //��������ΪName��Ԫ��
            name = doc.createElement("Name");
            //��������Ϊ ���� ���ı��ڵ㲢��Ϊ�ӽڵ���ӵ�nameԪ����
            name.appendChild(doc.createTextNode("����"));
            //��name��Ԫ����ӵ�student��
            student.appendChild(name);
            /**
             * �����Ԫ�����μ��뼴��
             * */
            num = doc.createElement("Num");
            num.appendChild(doc.createTextNode("1006010066"));
            student.appendChild(num);
            
            classes = doc.createElement("Classes");
            classes.appendChild(doc.createTextNode("���ӹ�5"));
            student.appendChild(classes);
            
            address = doc.createElement("Address");
            address.appendChild(doc.createTextNode("�㽭����"));
            student.appendChild(address);
            
            tel = doc.createElement("Tel");
            tel.appendChild(doc.createTextNode("123890"));
            student.appendChild(tel);
            
            //��student��Ϊ��Ԫ����ӵ����ĸ��ڵ�school
            school.appendChild(student);
            //���ڴ��е��ĵ�ͨ���ļ�������insertSchool.xml,XmlDocumentλ��crison.jar��
//            ((XmlDocument)doc).write(new FileOutputStream("insertSchool.xml"));
            ((XmlDocument)doc).write(new FileOutputStream("insertSchool.xml"));
            System.out.println("�ɹ�");
        }catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        }    
    }
    public static void main(String[] args){
        //��ȡ
        DomDemo.queryXml();
        //����
        DomDemo.insertXml();
    }
}