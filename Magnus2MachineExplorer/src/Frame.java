//import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.LayoutManager;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

class MainFrame extends JFrame
{
	private static final long serialVersionUID = 1L;
	
	ActionListener al1 = new ActionListener()
	{
		public void actionPerformed(ActionEvent arg0) {
			
		}
	};
	
	LayoutManager lm1 = new GridLayout(3,2);
	JPanel jpmain = new JPanel();
	JPanel jp1 = new JPanel();
	JPanel jp2 = new JPanel();
	JPanel jp3 = new JPanel();
	JPanel jp4 = new JPanel();
	JButton jb1 = new JButton();
//	JLabel jl = new JLabel();
	
	public void textbuilt()
	{
		jb1.setText($.$("msg1"));
	}
	MainFrame()
	{
		jb1.addActionListener(al1);
		
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setResizable(false);
		this.setUndecorated(false);
		this.setBounds(
				(int)Toolkit.getDefaultToolkit().getScreenSize().getWidth()/2-300,
				(int)Toolkit.getDefaultToolkit().getScreenSize().getHeight()/2-240,
				600,480);
		this.setTitle("Magnus2 Machine Explorer");
		
//		jl.setText("Ò»¸ö±êÇ©");
//		jl.setVerticalAlignment(JLabel.CENTER);
//		jl.setHorizontalAlignment(JLabel.CENTER);
		jb1.setMnemonic('Q');
		textbuilt();
		
		jpmain.setLayout(lm1);
		jp1.add(jb1);
		jpmain.add(jp1);
		jpmain.add(jp2);
		jpmain.add(jp3);
		jpmain.add(jp4);
		this.add(jpmain);
	}
}
