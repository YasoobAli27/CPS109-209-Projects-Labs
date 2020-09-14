// Syed Yasoob Ali
// 500953533

//Parent class to 2 subclasses: ActiveCourse and CreditCourse
public class Course 
{
	private String code;
	private String name;
	private String description;
	private String format;
	
	//initializes all variables as empty
	public Course()
	{
	  this.code        = "";
	  this.name        = "";
	  this.description = "";
	  this.format      = "";
	}
	
	//Course constructor takes in several parameters
	public Course(String name, String code, String descr, String fmt)
	{
	  this.code        = code;
	  this.name        = name;
	  this.description = descr;
	  this.format      = fmt;
	}
	   
	//Gets the class code and returns it
	public String getCode()
	{
	   return code;
	}
	   
	//Gets the class name and returns it
	public String getName()
	{
	  return name;
	}
	
	//Gets the class format and returns it
	public String getFormat()
	{
	  return format;
	}
	   
	//Gets the description of the course and returns it along with name and format
	public String getDescription()
	{
	  return code +" - " + name + "\n" + description + "\n" + format;
	}
	
	//Gets code and name of course
	public String getInfo()
	{
	  return code +" - " + name;
	}
	 
	 // static method to convert numeric score to letter grade string 
	 // e.g. 91 --> "A+"
	 
	 //Will convert the grade from a double to a string ranging from A+ - F.
	 public static String convertNumericGrade(double score)
	 {
		 // fill in code
		 
		 //Based on value of score, will conver to a letter grade and return it
		 if (score >= 90 && score <= 100)
		 {
			 return "A+";
		 }
		 else if (score >= 85 && score <= 89)
		 {
			 return "A";
		 }
		 else if (score >= 80 && score <= 84)
		 {
			 return "A-";
		 }
		 else if (score >= 77 && score <= 79)
		 {
			 return "B+";
		 }
		 else if (score >= 73 && score <= 76)
		 {
			 return "B";
		 }
		 else if (score >= 70 && score <= 72)
		 {
			 return "B-";
		 }
		 else if (score >= 67 && score <= 69)
		 {
			 return "C+";
		 }
		 else if (score >= 63 && score <= 66)
		 {
			 return "C";
		 }
		 else if (score >= 60 && score <= 62)
		 {
			 return "C-";
		 }
		 else if (score >= 57 && score <= 59)
		 {
			 return "D+";
		 }
		 else if (score >= 53 && score <= 56)
		 {
			 return "D";
		 }
		 else if (score >= 50 && score <= 52)
		 {
			 return "D-";
		 }
		 else
		 {
			 return "F";
		 }
		 
	 }
	 
}
