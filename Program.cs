

// Quiz application

namespace QuizApplication
{
    public class QuizApplication()
    {
        static void Main(string[] args)
        {
            var quiz = new Dictionary<string, string>()
            {
                {
                    "What is computer?", "one"
                },
                {
                    "ASCII","Yes"
                }
            };

            int score = 0;
            int incorretAnswered = 0;
            foreach (var item in quiz)
            {
                Console.Write($"{item.Key}: ");
                var userChoice = Console.ReadLine();
                if (userChoice == item.Value)
                {
                    score++;
                    Console.WriteLine("Correct Answer!");
                }
                else
                {
                    incorretAnswered++;
                    Console.WriteLine("Incorrect!");
                }
            }
            Console.WriteLine($"Total Score: {score}");


        }

    }
}