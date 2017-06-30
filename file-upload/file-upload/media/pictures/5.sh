echo "enter the password:"
read pass1
echo "renter the password:"
read pass2
if [ $pass1 = $pass2 ]
then
	echo "terminal is locked"
	trap '' 2 3 15
	while true
	do
		echo "enter the password"
		read pass3
		if [ $pass3 = $pass1 ]
		then
			echo "the terminal is unlocked"
			exit
		else
			echo "wrong password"
		fi
	done
else
echo "passwords do not match"
fi
