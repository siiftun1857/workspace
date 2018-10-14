import java.io.File;
import java.io.FileWriter;

import javax.swing.JFileChooser;
import javax.swing.filechooser.FileFilter;
import javax.swing.UIManager;

public class TestJFileChooser {

	public static void main(String[] args) {
		if(UIManager.getLookAndFeel().isSupportedLookAndFeel()){
			final String platform = UIManager.getSystemLookAndFeelClassName();
			// If the current Look & Feel does not match the platform Look & Feel,
			// change it so it does.
			if (!UIManager.getLookAndFeel().getName().equals(platform)) {
				try {
					UIManager.setLookAndFeel(platform);
				} catch (Exception exception) {
					exception.printStackTrace();
				}
			}
		}
		
		FileFilter ff = new FileFilter()
		{
			public boolean accept(java.io.File f) {
				if (f.isDirectory())return true;
					return f.getName().endsWith(".txt");  //设置为选择以.class为后缀的文件
			}

			public String getDescription() {
				return ".txt";
			}
		} ;

		JFileChooser fd = new JFileChooser();  
		fd.setFileFilter(ff);   //对JFileChooser设置过滤器
		//fd.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);  
		fd.showOpenDialog(null);  
		File f = fd.getSelectedFile();  
		if(f != null){}  
		
		JFileChooser jf = new JFileChooser();  
//		jf.setFileFilter(ff);   //对JFileChooser设置过滤器
		jf.setFileSelectionMode(JFileChooser.SAVE_DIALOG/* | JFileChooser.DIRECTORIES_ONLY*/);  
		jf.showDialog(null,null);  
		File fi = jf.getSelectedFile();  
		String f1 = fi.getAbsolutePath()+"\\test.txt";  
		System.out.println("save: "+f1);  
		try{  
			FileWriter out = new FileWriter(f1);  
			out.write("successful!!!");  
			out.close();  
		}  
		catch(Exception e){}  

	}

}
