package a;

public class Class1{
	protected int a;
	static
	{
		System.out.println("aaa");
	}
	public Class1()
	{
		this.a=0;
	}
	public Class1(int a)
	{
		this.a=a;
	}
	public int get()
	{
		return a;
	}
	public String toString()
	{
		return getClass().getName() + '@' + Integer.toHexString(hashCode());
	}
	public boolean equals(Object obj)
	{
		return (this == obj);
	}
}

