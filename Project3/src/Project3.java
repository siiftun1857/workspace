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
		System.out.println("���ڱ�����");
	}

	public void windowClosed(WindowEvent arg0) {
		System.out.println("���ڹر�");
	}

	public void windowClosing(WindowEvent arg0) {
		System.out.println("���ڳ��Թر�");
	}

	public void windowDeactivated(WindowEvent arg0) {
		System.out.println("����ʧȥ����");
	}

	public void windowDeiconified(WindowEvent arg0) {
		System.out.println("����ȡ����С��");
	}

	public void windowIconified(WindowEvent arg0) {
		System.out.println("������С��");
	}

	public void windowOpened(WindowEvent arg0) {
		System.out.println("�����״οɼ�");
	}

	public void windowGainedFocus(WindowEvent arg0) {
		System.out.println("���ڻ�ȡ����");
	}

	public void windowLostFocus(WindowEvent arg0) {
		System.out.println("����ʧȥ����");
	}
	
	private int i = 0;
	ActionListener al1 = new ActionListener()
	{
		public void actionPerformed(ActionEvent arg0) {
			((AbstractButton) arg0.getSource()).setText("��ť������"+(++i)+"��");
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
		
//		jl.setText("һ����ǩ");
//		jl.setVerticalAlignment(JLabel.CENTER);
//		jl.setHorizontalAlignment(JLabel.CENTER);
		jb1.setMnemonic('F');
//		jb2.setMnemonic('F');
		jb1.setText("��ť������"+i+"��");
		jb2.setText("����");
		
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
