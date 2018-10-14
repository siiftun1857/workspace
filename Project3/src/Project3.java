import java.awt.FlowLayout;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowFocusListener;
import java.awt.event.WindowListener;
import javax.swing.*;

class Swing1 extends JFrame implements WindowFocusListener ,WindowListener
{
	
	private static final long serialVersionUID = 1L;
	
	public void windowActivated(WindowEvent arg0) {
		System.out.println("窗口被激活");
	}

	public void windowClosed(WindowEvent arg0) {
		System.out.println("窗口关闭");
	}

	public void windowClosing(WindowEvent arg0) {
		System.out.println("窗口尝试关闭");
	}

	public void windowDeactivated(WindowEvent arg0) {
		System.out.println("窗口失去激活");
	}

	public void windowDeiconified(WindowEvent arg0) {
		System.out.println("窗口取消最小化");
	}

	public void windowIconified(WindowEvent arg0) {
		System.out.println("窗口最小化");
	}

	public void windowOpened(WindowEvent arg0) {
		System.out.println("窗口首次可见");
	}

	public void windowGainedFocus(WindowEvent arg0) {
		System.out.println("窗口获取焦点");
	}

	public void windowLostFocus(WindowEvent arg0) {
		System.out.println("窗口失去焦点");
	}
	
	private int i = 0;
	ActionListener al1 = new ActionListener()
	{
		public void actionPerformed(ActionEvent arg0) {
			((AbstractButton) arg0.getSource()).setText("按钮按下了"+(++i)+"次");
		}
	};
	ActionListener al2 = new ActionListener()
	{
		public void actionPerformed(ActionEvent arg0) {
			setResizable(!isResizable());
		}
	};
	
	FlowLayout fl1 = new FlowLayout();
	JPanel jp = new JPanel();
	JButton jb1 = new JButton();
	JButton jb2 = new JButton();
//	JLabel jl = new JLabel();
	
	Swing1()
	{
		this.addWindowListener(this);
		this.addWindowFocusListener(this);
		jb1.addActionListener(al1);
		jb2.addActionListener(al2);
		
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setResizable(false);
		this.setUndecorated(false);
		this.setBounds(
				(int)Toolkit.getDefaultToolkit().getScreenSize().getWidth()/2-300,
				(int)Toolkit.getDefaultToolkit().getScreenSize().getHeight()/2-240,
				600,480);
		this.setTitle("Project3");
		
//		jl.setText("一个标签");
//		jl.setVerticalAlignment(JLabel.CENTER);
//		jl.setHorizontalAlignment(JLabel.CENTER);
		jb1.setMnemonic('F');
//		jb2.setMnemonic('F');
		jb1.setText("按钮按下了"+i+"次");
		jb2.setText("缩放");
		
		jp.setLayout(fl1);
		jp.add(jb1);
		jp.add(jb2);
		this.add(jp);
		this.setVisible(true);
	}
}

public class Project3 {

	public static void main(String[] args) {
		@SuppressWarnings("unused")
		JFrame s1 = new Swing1();
	}
}
