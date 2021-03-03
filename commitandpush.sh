# A shell script for easier commit operations and pushing to remote repositories
# made by theroyakash

banner()
{
  echo "+------------------------------------------+"
  printf "| %-40s |\n" "`date`"
  printf "| %-40s |\n" "Made by theroyakash"
  echo "|                                          |"
  printf "|`tput bold` %-40s `tput sgr0`|\n" "$@"
  echo "+------------------------------------------+"
}

banner "Starting the Commit Job"


read -p "Commit Message: " cmessage

read -p "Continue commiting $cmessage? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

git add -A # Add all the files
git commit -m "$cmessage"
git push