using UnityEngine;
using System.Collections;
using System.Diagnostics;
using System.IO;
using TMPro;
using UnityEngine.UI;


public class solanaAPI : MonoBehaviour {

    public string getBalance(string wallet){
        Process process = new Process();
        process.StartInfo.FileName = "main.exe";
        process.StartInfo.Arguments = "getbalance "+ wallet;
        process.StartInfo.CreateNoWindow = true;
        process.StartInfo.UseShellExecute = false; // Required for redirection
        process.StartInfo.RedirectStandardOutput = true; // Redirect output
        process.Start();
        string balance = process.StandardOutput.ReadToEnd(); // Read the output
        process.WaitForExit(); // Wait for the process to finish
        process.Close(); // Close the process
        return balance;
        
    }

    // generate a wallet and return it
    public string GenerateWallet(){
        Process process = new Process();
        process.StartInfo.FileName = "main.exe";
        process.StartInfo.Arguments = "generateWallet";
        process.StartInfo.CreateNoWindow = true;
        process.StartInfo.UseShellExecute = false; // Required for redirection
        process.StartInfo.RedirectStandardOutput = true; // Redirect output
        process.Start();
        string keypair = process.StandardOutput.ReadToEnd(); // Read the output
        process.WaitForExit(); // Wait for the process to finish
        process.Close(); // Close the process
        return keypair;
    }

    public string Transfer(){
        return "test";
    }

}