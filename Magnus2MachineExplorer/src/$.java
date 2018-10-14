import java.util.Locale;
import java.util.MissingResourceException;
import java.util.ResourceBundle;

public final class $ {
	
	private static Locale locale = Locale.getDefault();
	
	private $()
	{
		throw new Error();
	}
	
	public static Locale Locale()
	{
		return locale;
	}
	
	public static Locale Locale(Locale locale)
	{
		return $.locale = locale;
	}
	@SuppressWarnings("all")
	public static String $(String str)
	{
		try
		{
			return ResourceBundle.getBundle("resources.res", locale).getString(str);
		}
		catch(MissingResourceException e)
		{
			try
			{
				return ResourceBundle.getBundle("resources.res", Locale.getDefault()).getString(str);
			}
			catch(MissingResourceException e1)
			{
				return str;
			}
		}
	}

}
