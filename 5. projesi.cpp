#include <iostream>
#include <string>
using namespace std;
// Base class: Person
class Person {
    protected:
    string name;
    int age;

public:
// Constructor
Person(const string& name,int age): name(name), age(age)
{}
// Method to display information
virtual void displayInfo() const {
    cout <<"Ad:" << name << ", Yas:" << age << endl;
}
// virtual destructor
virtual ~Person() {}
};
// Derived class: Student
class Student:public Person{
    private:
    int studentNumber;
public:
// constructor
Student(const string& name,int age,int StudentNumber)
:Person(name,age),studentNumber(studentNumber){}
// Method to display information
void displayInfo() const override{
    cout <<"ogrenci -> Ad:"<< name <<",Yas:"<< age
    <<",Numara:" << studentNumber << endl;
}
};
// Derived class: Teacher
class Teacher: public Person{
    private:
    string subject;
public:
// Constructor
Teacher(const string& name,int age,const string& subject)
  :Person(name,age),subject(subject){}
// Method to display information
void displayInfo() const override{
    cout <<"Ogretmen -> Ad:" << name <<",Yas:" << age <<",Ders:" << subject << endl;
}
};
// Main function
int main() {
    // Create a student object
    Student student("Ali",20, 12345);
    student.displayInfo();
// Create a Teacher object
Teacher teacher("Elzem", 35, "Tarih");
teacher.displayInfo();
return 0;

}













