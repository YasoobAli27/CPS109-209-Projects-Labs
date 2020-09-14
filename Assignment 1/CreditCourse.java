// Syed Yasoob Ali
// 500953533

//CreditCourse is an extension of Course
public class CreditCourse extends Course
{
	// add a constructor method with appropriate parameters
	// should call the super class constructor
	private String semester;
	public double grade;
	public boolean active;
	
	//Constructor method with the following parameters
	//Will super call the Course class to use name, code, description and format
	public CreditCourse(String name, String code, String descr, String fmt,String semester, double grade)
	{
		// add code
		super(name, code, descr, fmt);
		this.semester = semester;
		//Initializes grade to 0 and active to true 
		grade = 0;
		active = true;
		
	}
	
	//Returns if the course is currently active or not
	public boolean getActive()
	{
		return active;
	}
	
	//Sets the course to active, making it an ActiveCourse
	public void setActive()
	{
		active = true;
	}
	
	//Sets the course to inactive, making it a CreditCourse
	public void setInactive()
	{
		active = false;
	}
	
	//Displays the grade after converting it to a letter grade. Also displays info about course and semester.
	public String displayGrade()
	{
		// Change line below and print out info about this course plus which semester and the grade achieved
		// make use of inherited method in super class
		
		return(super.getInfo() + semester + super.convertNumericGrade(grade));
	}
	
}