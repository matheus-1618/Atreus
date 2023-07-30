## Ryuk Ransomware
> [!WARNING]    
> The threat analysed here is [available in Malware Baazar](https://bazaar.abuse.ch/browse.php?search=sha256%3A23F8AA94FFB3C08A62735FE7FEE5799880A8F322CE1D55EC49A13A3F85312DB2). Don't execute it in your host. Create a sandbox VirtualMachine in **VirtualBox**, **Paralells** or **VMWare** and take care about the execution of this ransomware, such as:
> 
> * Do not connect any host network during the execution to avoid connection with C&C;
> * Keep the virtualizer software updated;
> * Use a host OS different of the virtualized (e.g Linux as Host, and Windows in VM) to mitigate possible evasion;

### Ryuk Data 
You can see more about Ryuk in this folder, with informations collected during my Undergraduated Research about Ryuk (Reverse Engineering on it):
* Strings decoded and encoded in the dropper and payload;
* Ransom Note;
* Process Injection Routine in C++ used by Ryuk, discovered with Reverse Engineer with Xdbg64 and Snowman;
* Encryptation process, with data such as the Encryptation routine in C++ and ASM, the RSA1 key imported in my analysis and the CryptImportKey routine.

It has some typical behaviours analysed in this [research](/), such as:
* Multi-thread, calling CreateRemoteThread
* Process Injection through multiples process in the Machine
* AES256 encryption of files
* Envelope encryptation of each AES key inside the file with RSA1 key.
* Change of the registry keys using "svcho" for persistence
* Dropping it's executable in the "C:/Users/<user_name>/Public" folder

### About Ryuk
Ryuk ransomware is a sophisticated and notorious strain of ransomware that emerged in August 2018. It is known for its highly targeted attacks on large organizations, especially in the corporate and government sectors. Ryuk is believed to be operated by a cybercrime group known as Wizard Spider.

The primary purpose of Ryuk ransomware is to encrypt the victim's files, making them inaccessible. Once the files are encrypted, Ryuk displays a ransom note, typically in a "RyukReadMe.txt" file, containing instructions on how to pay the ransom to obtain the decryption key.

Key characteristics of Ryuk ransomware include:

1. Targeted Attacks: Ryuk targets specific organizations and infects their systems after gaining unauthorized access. These attacks often follow an initial infection by other malware, such as TrickBot or Emotet, which are used to gain a foothold in the network.

2. High Ransom Demands: Ryuk's ransom demands are usually significantly higher than those of other ransomware strains. This is because the attackers tailor the ransom amount based on the victim's perceived ability to pay, often demanding millions of dollars.

3. Manual Execution: Ryuk is often manually deployed by the attackers, enabling them to assess the network's value and select the most critical systems to target.

4. Custom Encryption: Ryuk employs a sophisticated encryption algorithm to lock files, making it challenging to decrypt them without the unique decryption key held by the attackers.

5. Evolving Tactics: The Ryuk ransomware is continually evolving, with the attackers refining their techniques to evade detection and increase their success rate.

It's important to note that paying the ransom does not guarantee that the attackers will provide the decryption key or that the files will be recovered. Moreover, it encourages and funds further criminal activities. To defend against ransomware attacks like Ryuk, organizations should focus on proactive cybersecurity measures, such as regular data backups, robust security protocols, and employee training to prevent phishing and social engineering attacks.



