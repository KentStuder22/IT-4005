//
//  ColorDetailViewController.swift
//  Colors
//
//  Created by Kent Studer on 3/10/21.
//

import UIKit

class ColorDetailViewController: UIViewController {
    
    var color: Color?
    
    @IBOutlet weak var label: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        label.text = color?.name
        
        self.view.backgroundColor = color?.uiColor
        
        self.title = color?.name
        // Do any additional setup after loading the view.
    }
    

}
