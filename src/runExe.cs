using UnityEngine;
using System.Collections;
using System.Diagnostics;

public class runExe : MonoBehaviour {

	// Use this for initialization
	void Start () {
		Process process = new Process();
		process.StartInfo.FileName = "connect.exe";
		process.StartInfo.Arguments = "";
        process.StartInfo.WindowStyle = ProcessWindowStyle.Normal;
		process.Start();

        
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
