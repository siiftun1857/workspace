import a.Class1;
import a.Class2;

public class Project1 {

	static void a()
	{
		System.out.println("a");
		b();
	}
	static void b()
	{
		System.out.println("b");
		a();
	}
	/**
	 * @author siiftun1857
	 * @param args
	 */
	public static void main(String[] args) {
		Class2 cls1 = new Class2(12);
		Class1 cls2 = new Class2();
		System.out.println("Number:"+cls1.get());
		System.out.println("Number:"+cls2.get());

		try
		{
			a();
		}
		catch(Throwable e)
		{
			System.err.println(e);
		}
		
		System.out.println("Number:"+1223);
	}

}
