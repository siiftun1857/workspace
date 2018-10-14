
class MyRunnable1 implements Runnable
{
	private long a;
	private String b;
	
	MyRunnable1(long a,String b)
	{
		this.a = a;
		this.b = b;
	}
	
	public void run() {
		while(true)
		{
			try {
		        Thread.sleep(a);
			} catch (InterruptedException e) {
		        e.printStackTrace();
			}
			System.out.print(b);
		}
	}
	
}

public class Project2 {
	public static void main(String[] args) {
		Thread t1 = new Thread(new MyRunnable1(1000,"a"));
		Thread t2 = new Thread(new MyRunnable1(2000,"b"));
	
		t1.start();
		t2.start();
		
	}
	
}
