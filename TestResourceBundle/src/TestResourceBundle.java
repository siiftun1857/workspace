import java.util.Locale; 
import java.util.ResourceBundle; 
/** 
* 国际化资源绑定测试
* 
* {@link http://lavasoft.blog.51cto.com/62575/184605/ }
* 
* @author leizhimin 2009-7-29 21:17:42 
*/ 
public class TestResourceBundle { 
	
	private static Locale MyLocale = Locale.getDefault();

	public static String $(String str)
	{
		return ResourceBundle.getBundle("resource.myres", MyLocale).getString(str);
	}
	
	public static void main(String[] args) { 
//			Locale locale1 = new Locale("zh", "CN"); 
			ResourceBundle resb1 = ResourceBundle.getBundle("resource.myres", Locale.CHINESE); 
			System.out.println(resb1.getString("aaa")); 
			
			ResourceBundle resb2 = ResourceBundle.getBundle("resource.myres", Locale.getDefault()); 
			System.out.println(resb2.getString("aaa")); 
			
//			Locale locale3 = new Locale("en", "US"); 
			ResourceBundle resb3 = ResourceBundle.getBundle("resource.myres", Locale.ENGLISH); 
			System.out.println(resb3.getString("aaa"));  
			
			System.out.println($("aaa"));  
			
			String[] str = Locale.getISOLanguages();
			for(int i = 0; i < str.length;i++)
            	System.out.print(new Locale(str[i]).getDisplayLanguage(new Locale(str[i]))+" "); 
	} 
}