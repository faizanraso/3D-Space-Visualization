import numpy as np
import open3d as o3d

if __name__ == "__main__":
    pcd = o3d.io.read_point_cloud("DATA.xyz", format='xyz')

    pt1 = 0
    pt2 = 1
    pt3 = 2
    pt4 = 3
    pt5 = 4
    pt6 = 5
    pt7 = 6
    pt8 = 7
    pt9 = 8
    pt10 = 9
    pt11 = 10
    pt12 = 11
    pt13 = 12
    pt14 = 13
    pt15 = 14
    pt16 = 15
    pt17 = 16
    pt18 = 17
    pt19 = 18
    pt20 = 19
    pt21 = 20
    pt22 = 21
    pt23 = 22
    pt24 = 23
    pt25 = 24
    pt26 = 25
    pt27 = 26
    pt28 = 27
    pt29 = 28
    pt30 = 29
    pt31 = 30
    pt32 = 31
    pt33 = 32
    pt34 = 33
    pt35 = 34
    pt36 = 35
    pt37 = 36
    pt38 = 37
    pt39 = 38
    pt40 = 39
    pt41 = 40
    pt42 = 41
    pt43 = 42
    pt44 = 43
    pt45 = 44
    pt46 = 45
    pt47 = 46
    pt48 = 47
    pt49 = 48
    pt50 = 49
    pt51 = 50
    pt52 = 51
    pt53 = 52
    pt54 = 53
    pt55 = 54
    pt56 = 55
    pt57 = 56
    pt58 = 57
    pt59 = 58
    pt60 = 59
    pt61 = 60
    pt62 = 61
    pt63 = 62
    pt64 = 63




    lines = []
    po = 0

    for x in range(10):
        lines.append([pt1+po, pt2+po])
        lines.append([pt2+po, pt3+po])
        lines.append([pt3+po, pt4+po])
        lines.append([pt4+po, pt5+po])
        lines.append([pt5+po, pt6+po])
        lines.append([pt6+po, pt7+po])
        lines.append([pt7+po, pt8+po])
        lines.append([pt8+po, pt9+po])
        lines.append([pt9+po, pt10+po])
        lines.append([pt10+po, pt11+po])
        lines.append([pt11+po, pt12+po])
        lines.append([pt12+po, pt13+po])
        lines.append([pt13+po, pt14+po])
        lines.append([pt14+po, pt15+po])
        lines.append([pt15+po, pt16+po])
        lines.append([pt16+po, pt17+po])
        lines.append([pt17+po, pt18+po])
        lines.append([pt18+po, pt19+po])
        lines.append([pt19+po, pt20+po])
        lines.append([pt20+po, pt21+po])
        lines.append([pt21+po, pt22+po])
        lines.append([pt22+po, pt23+po])
        lines.append([pt23+po, pt24+po])
        lines.append([pt24+po, pt25+po])
        lines.append([pt25+po, pt26+po])
        lines.append([pt26+po, pt27+po])
        lines.append([pt27+po, pt28+po])
        lines.append([pt28+po, pt29+po])
        lines.append([pt29+po, pt30+po])
        lines.append([pt30+po, pt31+po])
        lines.append([pt31+po, pt32+po])
        lines.append([pt32+po, pt1+po])
##        lines.append([pt33+po, pt34+po])
##        lines.append([pt34+po, pt35+po])
##        lines.append([pt35+po, pt36+po])
##        lines.append([pt36+po, pt37+po])
##        lines.append([pt37+po, pt38+po])
##        lines.append([pt38+po, pt39+po])
##        lines.append([pt39+po, pt40+po])
##        lines.append([pt40+po, pt41+po])
##        lines.append([pt41+po, pt42+po])
##        lines.append([pt42+po, pt43+po])
##        lines.append([pt43+po, pt44+po])
##        lines.append([pt44+po, pt45+po])
##        lines.append([pt45+po, pt46+po])
##        lines.append([pt46+po, pt47+po])
##        lines.append([pt47+po, pt48+po])
##        lines.append([pt48+po, pt49+po])
##        lines.append([pt49+po, pt50+po])
##        lines.append([pt50+po, pt51+po])
##        lines.append([pt51+po, pt52+po])
##        lines.append([pt52+po, pt53+po])
##        lines.append([pt53+po, pt54+po])
##        lines.append([pt54+po, pt55+po])
##        lines.append([pt55+po, pt56+po])
##        lines.append([pt56+po, pt57+po])
##        lines.append([pt57+po, pt58+po])
##        lines.append([pt58+po, pt59+po])
##        lines.append([pt59+po, pt60+po])
##        lines.append([pt60+po, pt61+po])
##        lines.append([pt61+po, pt62+po])
##        lines.append([pt62+po, pt63+po])
##        lines.append([pt63+po, pt64+po])
##        lines.append([pt64+po, pt1+po])

        po+=32 

    # reset variables
    pt1 = 0
    pt2 = 1
    pt3 = 2
    pt4 = 3
    pt5 = 4
    pt6 = 5
    pt7 = 6
    pt8 = 7
    pt9 = 8
    pt10 = 9
    pt11 = 10
    pt12 = 11
    pt13 = 12
    pt14 = 13
    pt15 = 14
    pt16 = 15
    pt17 = 16
    pt18 = 17
    pt19 = 18
    pt20 = 19
    pt21 = 20
    pt22 = 21
    pt23 = 22
    pt24 = 23
    pt25 = 24
    pt26 = 25
    pt27 = 26
    pt28 = 27
    pt29 = 28
    pt30 = 29
    pt31 = 30
    pt32 = 31
    pt33 = 32
    pt34 = 33
    pt35 = 34
    pt36 = 35
    pt37 = 36
    pt38 = 37
    pt39 = 38
    pt40 = 39
    pt41 = 40
    pt42 = 41
    pt43 = 42
    pt44 = 43
    pt45 = 44
    pt46 = 45
    pt47 = 46
    pt48 = 47
    pt49 = 48
    pt50 = 49
    pt51 = 50
    pt52 = 51
    pt53 = 52
    pt54 = 53
    pt55 = 54
    pt56 = 55
    pt57 = 56
    pt58 = 57
    pt59 = 58
    pt60 = 59
    pt61 = 60
    pt62 = 61
    pt63 = 62
    pt64 = 63
    
    po = 0
    do = 32 

    for x in range(9):
        lines.append([pt1+po, pt1+po+do])
        lines.append([pt2+po, pt2+po+do])
        lines.append([pt3+po, pt3+po+do])
        lines.append([pt4+po, pt4+po+do])
        lines.append([pt5+po, pt5+po+do])
        lines.append([pt6+po, pt6+po+do])
        lines.append([pt7+po, pt7+po+do])
        lines.append([pt8+po, pt8+po+do])
        lines.append([pt9+po, pt9+po+do])
        lines.append([pt10+po, pt10+po+do])
        lines.append([pt11+po, pt11+po+do])
        lines.append([pt12+po, pt12+po+do])
        lines.append([pt13+po, pt13+po+do])
        lines.append([pt14+po, pt14+po+do])
        lines.append([pt15+po, pt15+po+do])
        lines.append([pt16+po, pt16+po+do])
        lines.append([pt17+po, pt17+po+do])
        lines.append([pt18+po, pt18+po+do])
        lines.append([pt19+po, pt19+po+do])
        lines.append([pt20+po, pt20+po+do])
        lines.append([pt21+po, pt21+po+do])
        lines.append([pt22+po, pt22+po+do])
        lines.append([pt23+po, pt23+po+do])
        lines.append([pt24+po, pt24+po+do])
        lines.append([pt25+po, pt25+po+do])
        lines.append([pt26+po, pt26+po+do])
        lines.append([pt27+po, pt27+po+do])
        lines.append([pt28+po, pt28+po+do])
        lines.append([pt29+po, pt29+po+do])
        lines.append([pt30+po, pt30+po+do])
        lines.append([pt31+po, pt31+po+do])
        lines.append([pt32+po, pt32+po+do])
##        lines.append([pt33+po, pt34+po+do])
##        lines.append([pt34+po, pt35+po+do])
##        lines.append([pt35+po, pt36+po+do])
##        lines.append([pt36+po, pt37+po+do])
##        lines.append([pt37+po, pt38+po+do])
##        lines.append([pt38+po, pt39+po+do])
##        lines.append([pt39+po, pt40+po+do])
##        lines.append([pt40+po, pt41+po+do])
##        lines.append([pt41+po, pt42+po+do])
##        lines.append([pt42+po, pt43+po+do])
##        lines.append([pt43+po, pt44+po+do])
##        lines.append([pt44+po, pt45+po+do])
##        lines.append([pt45+po, pt46+po+do])
##        lines.append([pt46+po, pt47+po+do])
##        lines.append([pt47+po, pt48+po+do])
##        lines.append([pt48+po, pt49+po+do])
##        lines.append([pt49+po, pt50+po+do])
##        lines.append([pt50+po, pt51+po+do])
##        lines.append([pt51+po, pt52+po+do])
##        lines.append([pt52+po, pt53+po+do])
##        lines.append([pt53+po, pt54+po+do])
##        lines.append([pt54+po, pt55+po+do])
##        lines.append([pt55+po, pt56+po+do])
##        lines.append([pt56+po, pt57+po+do])
##        lines.append([pt57+po, pt58+po+do])
##        lines.append([pt58+po, pt59+po+do])
##        lines.append([pt59+po, pt60+po+do])
##        lines.append([pt60+po, pt61+po+do])
##        lines.append([pt61+po, pt62+po+do])
##        lines.append([pt62+po, pt63+po+do])
##        lines.append([pt63+po, pt64+po+do])
##        lines.append([pt64+po, pt64+po+do])
        po+=32
    

    line_set = o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pcd.points)), lines=o3d.utility.Vector2iVector(lines))
    o3d.visualization.draw_geometries([line_set])
    


