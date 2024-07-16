```mermaid
graph LR
    subgraph NG_BishopBlack
    style NG_BishopBlack_base_color_output  fill:#0C0, color:#FFF
    NG_BishopBlack_base_color_output([base_color_output])
    style NG_BishopBlack_metalness_output  fill:#0C0, color:#FFF
    NG_BishopBlack_metalness_output([metalness_output])
    style NG_BishopBlack_roughness_output  fill:#0C0, color:#FFF
    NG_BishopBlack_roughness_output([roughness_output])
    style NG_BishopBlack_normal_output  fill:#0C0, color:#FFF
    NG_BishopBlack_normal_output([normal_output])
    NG_BishopBlack_diffuse2[diffuse2:chess_set/bishop_black_base_color.jpg]
    NG_BishopBlack_metallic2[metallic2:chess_set/bishop_shared_metallic.jpg]
    NG_BishopBlack_roughness2[roughness2:chess_set/bishop_black_roughness.jpg]
    NG_BishopBlack_normal2[normal2:chess_set/bishop_black_normal.jpg]
    NG_BishopBlack_mtlxnormalmap4[mtlxnormalmap4]
    end
    Bishop_B[Bishop_B]
    style M_Bishop_B  fill:#090, color:#FFF
    M_Bishop_B([M_Bishop_B])
    Bishop_W[Bishop_W]
    style M_Bishop_W  fill:#090, color:#FFF
    M_Bishop_W([M_Bishop_W])
    Castle_B[Castle_B]
    style M_Castle_B  fill:#090, color:#FFF
    M_Castle_B([M_Castle_B])
    Castle_W[Castle_W]
    style M_Castle_W  fill:#090, color:#FFF
    M_Castle_W([M_Castle_W])
    Chessboard[Chessboard]
    style M_Chessboard  fill:#090, color:#FFF
    M_Chessboard([M_Chessboard])
    King_B[King_B]
    style M_King_B  fill:#090, color:#FFF
    M_King_B([M_King_B])
    King_W[King_W]
    style M_King_W  fill:#090, color:#FFF
    M_King_W([M_King_W])
    Knight_B[Knight_B]
    style M_Knight_B  fill:#090, color:#FFF
    M_Knight_B([M_Knight_B])
    Knight_W[Knight_W]
    style M_Knight_W  fill:#090, color:#FFF
    M_Knight_W([M_Knight_W])
    Pawn_Body_B[Pawn_Body_B]
    style M_Pawn_Body_B  fill:#090, color:#FFF
    M_Pawn_Body_B([M_Pawn_Body_B])
    Pawn_Body_W[Pawn_Body_W]
    style M_Pawn_Body_W  fill:#090, color:#FFF
    M_Pawn_Body_W([M_Pawn_Body_W])
    Pawn_Top_B[Pawn_Top_B]
    style M_Pawn_Top_B  fill:#090, color:#FFF
    M_Pawn_Top_B([M_Pawn_Top_B])
    Pawn_Top_W[Pawn_Top_W]
    style M_Pawn_Top_W  fill:#090, color:#FFF
    M_Pawn_Top_W([M_Pawn_Top_W])
    Queen_B[Queen_B]
    style M_Queen_B  fill:#090, color:#FFF
    M_Queen_B([M_Queen_B])
    Queen_W[Queen_W]
    style M_Queen_W  fill:#090, color:#FFF
    M_Queen_W([M_Queen_W])
    subgraph NG_BishopWhite
    style NG_BishopWhite_base_color_output  fill:#0C0, color:#FFF
    NG_BishopWhite_base_color_output([base_color_output])
    style NG_BishopWhite_metalness_output  fill:#0C0, color:#FFF
    NG_BishopWhite_metalness_output([metalness_output])
    style NG_BishopWhite_roughness_output  fill:#0C0, color:#FFF
    NG_BishopWhite_roughness_output([roughness_output])
    style NG_BishopWhite_normal_output  fill:#0C0, color:#FFF
    NG_BishopWhite_normal_output([normal_output])
    NG_BishopWhite_diffuse3[diffuse3:chess_set/bishop_white_base_color.jpg]
    NG_BishopWhite_metallic3[metallic3:chess_set/bishop_shared_metallic.jpg]
    NG_BishopWhite_roughness3[roughness3:chess_set/bishop_white_roughness.jpg]
    NG_BishopWhite_normal3[normal3:chess_set/bishop_white_normal.jpg]
    NG_BishopWhite_mtlxnormalmap5[mtlxnormalmap5]
    end
    subgraph NG_CastleBlack
    style NG_CastleBlack_base_color_output  fill:#0C0, color:#FFF
    NG_CastleBlack_base_color_output([base_color_output])
    style NG_CastleBlack_metalness_output  fill:#0C0, color:#FFF
    NG_CastleBlack_metalness_output([metalness_output])
    style NG_CastleBlack_roughness_output  fill:#0C0, color:#FFF
    NG_CastleBlack_roughness_output([roughness_output])
    style NG_CastleBlack_normal_output  fill:#0C0, color:#FFF
    NG_CastleBlack_normal_output([normal_output])
    NG_CastleBlack_diffuse6[diffuse6:chess_set/castle_black_base_color.jpg]
    NG_CastleBlack_metallic6[metallic6:chess_set/castle_shared_metallic.jpg]
    NG_CastleBlack_roughness6[roughness6:chess_set/castle_shared_roughness.jpg]
    NG_CastleBlack_normal6[normal6:chess_set/castle_shared_normal.jpg]
    NG_CastleBlack_mtlxnormalmap8[mtlxnormalmap8]
    end
    subgraph NG_CastleWhite
    style NG_CastleWhite_base_color_output  fill:#0C0, color:#FFF
    NG_CastleWhite_base_color_output([base_color_output])
    style NG_CastleWhite_metalness_output  fill:#0C0, color:#FFF
    NG_CastleWhite_metalness_output([metalness_output])
    style NG_CastleWhite_roughness_output  fill:#0C0, color:#FFF
    NG_CastleWhite_roughness_output([roughness_output])
    style NG_CastleWhite_normal_output  fill:#0C0, color:#FFF
    NG_CastleWhite_normal_output([normal_output])
    NG_CastleWhite_diffuse7[diffuse7:chess_set/castle_white_base_color.jpg]
    NG_CastleWhite_metallic7[metallic7:chess_set/castle_shared_metallic.jpg]
    NG_CastleWhite_roughness7[roughness7:chess_set/castle_shared_roughness.jpg]
    NG_CastleWhite_normal7[normal7:chess_set/castle_shared_normal.jpg]
    NG_CastleWhite_mtlxnormalmap9[mtlxnormalmap9]
    end
    subgraph NG_ChessBoard
    style NG_ChessBoard_base_color_output  fill:#0C0, color:#FFF
    NG_ChessBoard_base_color_output([base_color_output])
    style NG_ChessBoard_metalness_output  fill:#0C0, color:#FFF
    NG_ChessBoard_metalness_output([metalness_output])
    style NG_ChessBoard_roughness_output  fill:#0C0, color:#FFF
    NG_ChessBoard_roughness_output([roughness_output])
    style NG_ChessBoard_normal_output  fill:#0C0, color:#FFF
    NG_ChessBoard_normal_output([normal_output])
    NG_ChessBoard_mtlximage13[mtlximage13:chess_set/chessboard_base_color.jpg]
    NG_ChessBoard_mtlximage16[mtlximage16:chess_set/chessboard_metallic.jpg]
    NG_ChessBoard_mtlximage17[mtlximage17:chess_set/chessboard_roughness.jpg]
    NG_ChessBoard_mtlximage15[mtlximage15:chess_set/chessboard_normal.jpg]
    NG_ChessBoard_mtlxnormalmap12[mtlxnormalmap12]
    end
    subgraph NG_KingBlack
    style NG_KingBlack_base_color_output  fill:#0C0, color:#FFF
    NG_KingBlack_base_color_output([base_color_output])
    style NG_KingBlack_metalness_output  fill:#0C0, color:#FFF
    NG_KingBlack_metalness_output([metalness_output])
    style NG_KingBlack_roughness_output  fill:#0C0, color:#FFF
    NG_KingBlack_roughness_output([roughness_output])
    style NG_KingBlack_subsurface_output  fill:#0C0, color:#FFF
    NG_KingBlack_subsurface_output([subsurface_output])
    style NG_KingBlack_normal_output  fill:#0C0, color:#FFF
    NG_KingBlack_normal_output([normal_output])
    NG_KingBlack_mtlximage1[mtlximage1:chess_set/king_black_base_color.jpg]
    NG_KingBlack_mtlximage2[mtlximage2:chess_set/king_shared_metallic.jpg]
    NG_KingBlack_mtlximage4[mtlximage4:chess_set/king_black_roughness.jpg]
    NG_KingBlack_mtlximage3[mtlximage3:chess_set/king_shared_scattering.jpg]
    NG_KingBlack_mtlximage6[mtlximage6:chess_set/king_black_normal.jpg]
    NG_KingBlack_mtlxnormalmap1[mtlxnormalmap1]
    end
    subgraph NG_KingWhite
    style NG_KingWhite_base_color_output  fill:#0C0, color:#FFF
    NG_KingWhite_base_color_output([base_color_output])
    style NG_KingWhite_metalness_output  fill:#0C0, color:#FFF
    NG_KingWhite_metalness_output([metalness_output])
    style NG_KingWhite_roughness_output  fill:#0C0, color:#FFF
    NG_KingWhite_roughness_output([roughness_output])
    style NG_KingWhite_subsurface_output  fill:#0C0, color:#FFF
    NG_KingWhite_subsurface_output([subsurface_output])
    style NG_KingWhite_normal_output  fill:#0C0, color:#FFF
    NG_KingWhite_normal_output([normal_output])
    NG_KingWhite_mtlximage7[mtlximage7:chess_set/king_white_base_color.jpg]
    NG_KingWhite_mtlximage10[mtlximage10:chess_set/king_shared_metallic.jpg]
    NG_KingWhite_mtlximage11[mtlximage11:chess_set/king_white_roughness.jpg]
    NG_KingWhite_mtlximage8[mtlximage8:chess_set/king_shared_scattering.jpg]
    NG_KingWhite_mtlximage9[mtlximage9:chess_set/king_white_normal.jpg]
    NG_KingWhite_mtlxnormalmap11[mtlxnormalmap11]
    end
    subgraph NG_KnightBlack
    style NG_KnightBlack_base_color_output  fill:#0C0, color:#FFF
    NG_KnightBlack_base_color_output([base_color_output])
    style NG_KnightBlack_roughness_output  fill:#0C0, color:#FFF
    NG_KnightBlack_roughness_output([roughness_output])
    style NG_KnightBlack_normal_output  fill:#0C0, color:#FFF
    NG_KnightBlack_normal_output([normal_output])
    NG_KnightBlack_diffuse4[diffuse4:chess_set/knight_black_base_color.jpg]
    NG_KnightBlack_roughness4[roughness4:chess_set/knight_black_roughness.jpg]
    NG_KnightBlack_normal4[normal4:chess_set/knight_black_normal.jpg]
    NG_KnightBlack_mtlxnormalmap6[mtlxnormalmap6]
    end
    subgraph NG_KnightWhite
    style NG_KnightWhite_base_color_output  fill:#0C0, color:#FFF
    NG_KnightWhite_base_color_output([base_color_output])
    style NG_KnightWhite_roughness_output  fill:#0C0, color:#FFF
    NG_KnightWhite_roughness_output([roughness_output])
    style NG_KnightWhite_normal_output  fill:#0C0, color:#FFF
    NG_KnightWhite_normal_output([normal_output])
    NG_KnightWhite_diffuse5[diffuse5:chess_set/knight_white_base_color.jpg]
    NG_KnightWhite_roughness5[roughness5:chess_set/knight_white_roughness.jpg]
    NG_KnightWhite_normal5[normal5:chess_set/knight_white_normal.jpg]
    NG_KnightWhite_mtlxnormalmap7[mtlxnormalmap7]
    end
    subgraph NG_PawnBodyBlack
    style NG_PawnBodyBlack_base_color_output  fill:#0C0, color:#FFF
    NG_PawnBodyBlack_base_color_output([base_color_output])
    style NG_PawnBodyBlack_metalness_output  fill:#0C0, color:#FFF
    NG_PawnBodyBlack_metalness_output([metalness_output])
    style NG_PawnBodyBlack_roughness_output  fill:#0C0, color:#FFF
    NG_PawnBodyBlack_roughness_output([roughness_output])
    style NG_PawnBodyBlack_normal_output  fill:#0C0, color:#FFF
    NG_PawnBodyBlack_normal_output([normal_output])
    NG_PawnBodyBlack_diffuse9[diffuse9:chess_set/pawn_black_base_color.jpg]
    NG_PawnBodyBlack_metallic9[metallic9:chess_set/pawn_shared_metallic.jpg]
    NG_PawnBodyBlack_roughness9[roughness9:chess_set/pawn_shared_roughness.jpg]
    NG_PawnBodyBlack_normal9[normal9:chess_set/pawn_shared_normal.jpg]
    NG_PawnBodyBlack_mtlxnormalmap13[mtlxnormalmap13]
    end
    subgraph NG_PawnBodyWhite
    style NG_PawnBodyWhite_base_color_output  fill:#0C0, color:#FFF
    NG_PawnBodyWhite_base_color_output([base_color_output])
    style NG_PawnBodyWhite_metalness_output  fill:#0C0, color:#FFF
    NG_PawnBodyWhite_metalness_output([metalness_output])
    style NG_PawnBodyWhite_roughness_output  fill:#0C0, color:#FFF
    NG_PawnBodyWhite_roughness_output([roughness_output])
    style NG_PawnBodyWhite_normal_output  fill:#0C0, color:#FFF
    NG_PawnBodyWhite_normal_output([normal_output])
    NG_PawnBodyWhite_diffuse8[diffuse8:chess_set/pawn_white_base_color.jpg]
    NG_PawnBodyWhite_metallic8[metallic8:chess_set/pawn_shared_metallic.jpg]
    NG_PawnBodyWhite_roughness8[roughness8:chess_set/pawn_shared_roughness.jpg]
    NG_PawnBodyWhite_normal8[normal8:chess_set/pawn_shared_normal.jpg]
    NG_PawnBodyWhite_mtlxnormalmap10[mtlxnormalmap10]
    end
    subgraph NG_PawnTopBlack
    style NG_PawnTopBlack_roughness_output  fill:#0C0, color:#FFF
    NG_PawnTopBlack_roughness_output([roughness_output])
    style NG_PawnTopBlack_normal_output  fill:#0C0, color:#FFF
    NG_PawnTopBlack_normal_output([normal_output])
    NG_PawnTopBlack_mtlximage19[mtlximage19:chess_set/pawn_shared_roughness.jpg]
    NG_PawnTopBlack_mtlximage18[mtlximage18:chess_set/pawn_shared_normal.jpg]
    NG_PawnTopBlack_mtlxnormalmap14[mtlxnormalmap14]
    end
    subgraph NG_PawnTopWhite
    style NG_PawnTopWhite_roughness_output  fill:#0C0, color:#FFF
    NG_PawnTopWhite_roughness_output([roughness_output])
    style NG_PawnTopWhite_normal_output  fill:#0C0, color:#FFF
    NG_PawnTopWhite_normal_output([normal_output])
    NG_PawnTopWhite_mtlximage21[mtlximage21:chess_set/pawn_shared_roughness.jpg]
    NG_PawnTopWhite_mtlximage20[mtlximage20:chess_set/pawn_shared_normal.jpg]
    NG_PawnTopWhite_mtlxnormalmap15[mtlxnormalmap15]
    end
    subgraph NG_QueenBlack
    style NG_QueenBlack_base_color_output  fill:#0C0, color:#FFF
    NG_QueenBlack_base_color_output([base_color_output])
    style NG_QueenBlack_metalness_output  fill:#0C0, color:#FFF
    NG_QueenBlack_metalness_output([metalness_output])
    style NG_QueenBlack_roughness_output  fill:#0C0, color:#FFF
    NG_QueenBlack_roughness_output([roughness_output])
    style NG_QueenBlack_subsurface_output  fill:#0C0, color:#FFF
    NG_QueenBlack_subsurface_output([subsurface_output])
    style NG_QueenBlack_normal_output  fill:#0C0, color:#FFF
    NG_QueenBlack_normal_output([normal_output])
    NG_QueenBlack_diffuse[diffuse:chess_set/queen_black_base_color.jpg]
    NG_QueenBlack_metallic[metallic:chess_set/queen_shared_metallic.jpg]
    NG_QueenBlack_roughness[roughness:chess_set/queen_black_roughness.jpg]
    NG_QueenBlack_sss[sss:chess_set/queen_shared_scattering.jpg]
    NG_QueenBlack_normal[normal:chess_set/queen_black_normal.jpg]
    NG_QueenBlack_mtlxnormalmap2[mtlxnormalmap2]
    end
    subgraph NG_QueenWhite
    style NG_QueenWhite_base_color_output  fill:#0C0, color:#FFF
    NG_QueenWhite_base_color_output([base_color_output])
    style NG_QueenWhite_metalness_output  fill:#0C0, color:#FFF
    NG_QueenWhite_metalness_output([metalness_output])
    style NG_QueenWhite_roughness_output  fill:#0C0, color:#FFF
    NG_QueenWhite_roughness_output([roughness_output])
    style NG_QueenWhite_subsurface_output  fill:#0C0, color:#FFF
    NG_QueenWhite_subsurface_output([subsurface_output])
    style NG_QueenWhite_normal_output  fill:#0C0, color:#FFF
    NG_QueenWhite_normal_output([normal_output])
    NG_QueenWhite_diffuse1[diffuse1:chess_set/queen_white_base_color.jpg]
    NG_QueenWhite_metallic1[metallic1:chess_set/queen_shared_metallic.jpg]
    NG_QueenWhite_roughness1[roughness1:chess_set/queen_white_roughness.jpg]
    NG_QueenWhite_sss1[sss1:chess_set/queen_shared_scattering.jpg]
    NG_QueenWhite_normal1[normal1:chess_set/queen_white_normal.jpg]
    NG_QueenWhite_mtlxnormalmap3[mtlxnormalmap3]
    end
    NG_BishopBlack_normal2 --"in"--> NG_BishopBlack_mtlxnormalmap4
    NG_BishopBlack_diffuse2 --> NG_BishopBlack_base_color_output
    NG_BishopBlack_metallic2 --> NG_BishopBlack_metalness_output
    NG_BishopBlack_roughness2 --> NG_BishopBlack_roughness_output
    NG_BishopBlack_mtlxnormalmap4 --> NG_BishopBlack_normal_output
    NG_BishopBlack_base_color_output --"base_color"--> Bishop_B
    NG_BishopBlack_metalness_output --"metalness"--> Bishop_B
    NG_BishopBlack_roughness_output --"specular_roughness"--> Bishop_B
    NG_BishopBlack_base_color_output --"subsurface_color"--> Bishop_B
    NG_BishopBlack_base_color_output --"subsurface_radius"--> Bishop_B
    NG_BishopBlack_normal_output --"normal"--> Bishop_B
    Bishop_B --"surfaceshader"--> M_Bishop_B
    NG_BishopWhite_normal3 --"in"--> NG_BishopWhite_mtlxnormalmap5
    NG_BishopWhite_diffuse3 --> NG_BishopWhite_base_color_output
    NG_BishopWhite_metallic3 --> NG_BishopWhite_metalness_output
    NG_BishopWhite_roughness3 --> NG_BishopWhite_roughness_output
    NG_BishopWhite_mtlxnormalmap5 --> NG_BishopWhite_normal_output
    NG_BishopWhite_base_color_output --"base_color"--> Bishop_W
    NG_BishopWhite_metalness_output --"metalness"--> Bishop_W
    NG_BishopWhite_roughness_output --"specular_roughness"--> Bishop_W
    NG_BishopWhite_base_color_output --"subsurface_color"--> Bishop_W
    NG_BishopWhite_base_color_output --"subsurface_radius"--> Bishop_W
    NG_BishopWhite_normal_output --"normal"--> Bishop_W
    Bishop_W --"surfaceshader"--> M_Bishop_W
    NG_CastleBlack_normal6 --"in"--> NG_CastleBlack_mtlxnormalmap8
    NG_CastleBlack_diffuse6 --> NG_CastleBlack_base_color_output
    NG_CastleBlack_metallic6 --> NG_CastleBlack_metalness_output
    NG_CastleBlack_roughness6 --> NG_CastleBlack_roughness_output
    NG_CastleBlack_mtlxnormalmap8 --> NG_CastleBlack_normal_output
    NG_CastleBlack_base_color_output --"base_color"--> Castle_B
    NG_CastleBlack_metalness_output --"metalness"--> Castle_B
    NG_CastleBlack_roughness_output --"specular_roughness"--> Castle_B
    NG_CastleBlack_base_color_output --"subsurface_color"--> Castle_B
    NG_CastleBlack_base_color_output --"subsurface_radius"--> Castle_B
    NG_CastleBlack_normal_output --"normal"--> Castle_B
    Castle_B --"surfaceshader"--> M_Castle_B
    NG_CastleWhite_normal7 --"in"--> NG_CastleWhite_mtlxnormalmap9
    NG_CastleWhite_diffuse7 --> NG_CastleWhite_base_color_output
    NG_CastleWhite_metallic7 --> NG_CastleWhite_metalness_output
    NG_CastleWhite_roughness7 --> NG_CastleWhite_roughness_output
    NG_CastleWhite_mtlxnormalmap9 --> NG_CastleWhite_normal_output
    NG_CastleWhite_base_color_output --"base_color"--> Castle_W
    NG_CastleWhite_metalness_output --"metalness"--> Castle_W
    NG_CastleWhite_roughness_output --"specular_roughness"--> Castle_W
    NG_CastleWhite_base_color_output --"subsurface_color"--> Castle_W
    NG_CastleWhite_base_color_output --"subsurface_radius"--> Castle_W
    NG_CastleWhite_normal_output --"normal"--> Castle_W
    Castle_W --"surfaceshader"--> M_Castle_W
    NG_ChessBoard_mtlximage15 --"in"--> NG_ChessBoard_mtlxnormalmap12
    NG_ChessBoard_mtlximage13 --> NG_ChessBoard_base_color_output
    NG_ChessBoard_mtlximage16 --> NG_ChessBoard_metalness_output
    NG_ChessBoard_mtlximage17 --> NG_ChessBoard_roughness_output
    NG_ChessBoard_mtlxnormalmap12 --> NG_ChessBoard_normal_output
    NG_ChessBoard_base_color_output --"base_color"--> Chessboard
    NG_ChessBoard_metalness_output --"metalness"--> Chessboard
    NG_ChessBoard_roughness_output --"specular_roughness"--> Chessboard
    NG_ChessBoard_base_color_output --"subsurface_color"--> Chessboard
    NG_ChessBoard_base_color_output --"subsurface_radius"--> Chessboard
    NG_ChessBoard_normal_output --"normal"--> Chessboard
    Chessboard --"surfaceshader"--> M_Chessboard
    NG_KingBlack_mtlximage6 --"in"--> NG_KingBlack_mtlxnormalmap1
    NG_KingBlack_mtlximage1 --> NG_KingBlack_base_color_output
    NG_KingBlack_mtlximage2 --> NG_KingBlack_metalness_output
    NG_KingBlack_mtlximage4 --> NG_KingBlack_roughness_output
    NG_KingBlack_mtlximage3 --> NG_KingBlack_subsurface_output
    NG_KingBlack_mtlxnormalmap1 --> NG_KingBlack_normal_output
    NG_KingBlack_base_color_output --"base_color"--> King_B
    NG_KingBlack_metalness_output --"metalness"--> King_B
    NG_KingBlack_roughness_output --"specular_roughness"--> King_B
    NG_KingBlack_subsurface_output --"subsurface"--> King_B
    NG_KingBlack_base_color_output --"subsurface_color"--> King_B
    NG_KingBlack_base_color_output --"subsurface_radius"--> King_B
    NG_KingBlack_normal_output --"normal"--> King_B
    King_B --"surfaceshader"--> M_King_B
    NG_KingWhite_mtlximage9 --"in"--> NG_KingWhite_mtlxnormalmap11
    NG_KingWhite_mtlximage7 --> NG_KingWhite_base_color_output
    NG_KingWhite_mtlximage10 --> NG_KingWhite_metalness_output
    NG_KingWhite_mtlximage11 --> NG_KingWhite_roughness_output
    NG_KingWhite_mtlximage8 --> NG_KingWhite_subsurface_output
    NG_KingWhite_mtlxnormalmap11 --> NG_KingWhite_normal_output
    NG_KingWhite_base_color_output --"base_color"--> King_W
    NG_KingWhite_metalness_output --"metalness"--> King_W
    NG_KingWhite_roughness_output --"specular_roughness"--> King_W
    NG_KingWhite_subsurface_output --"subsurface"--> King_W
    NG_KingWhite_base_color_output --"subsurface_color"--> King_W
    NG_KingWhite_base_color_output --"subsurface_radius"--> King_W
    NG_KingWhite_normal_output --"normal"--> King_W
    King_W --"surfaceshader"--> M_King_W
    NG_KnightBlack_normal4 --"in"--> NG_KnightBlack_mtlxnormalmap6
    NG_KnightBlack_diffuse4 --> NG_KnightBlack_base_color_output
    NG_KnightBlack_roughness4 --> NG_KnightBlack_roughness_output
    NG_KnightBlack_mtlxnormalmap6 --> NG_KnightBlack_normal_output
    NG_KnightBlack_base_color_output --"base_color"--> Knight_B
    NG_KnightBlack_roughness_output --"specular_roughness"--> Knight_B
    NG_KnightBlack_base_color_output --"subsurface_color"--> Knight_B
    NG_KnightBlack_base_color_output --"subsurface_radius"--> Knight_B
    NG_KnightBlack_normal_output --"normal"--> Knight_B
    Knight_B --"surfaceshader"--> M_Knight_B
    NG_KnightWhite_normal5 --"in"--> NG_KnightWhite_mtlxnormalmap7
    NG_KnightWhite_diffuse5 --> NG_KnightWhite_base_color_output
    NG_KnightWhite_roughness5 --> NG_KnightWhite_roughness_output
    NG_KnightWhite_mtlxnormalmap7 --> NG_KnightWhite_normal_output
    NG_KnightWhite_base_color_output --"base_color"--> Knight_W
    NG_KnightWhite_roughness_output --"specular_roughness"--> Knight_W
    NG_KnightWhite_base_color_output --"subsurface_color"--> Knight_W
    NG_KnightWhite_base_color_output --"subsurface_radius"--> Knight_W
    NG_KnightWhite_normal_output --"normal"--> Knight_W
    Knight_W --"surfaceshader"--> M_Knight_W
    NG_PawnBodyBlack_normal9 --"in"--> NG_PawnBodyBlack_mtlxnormalmap13
    NG_PawnBodyBlack_diffuse9 --> NG_PawnBodyBlack_base_color_output
    NG_PawnBodyBlack_metallic9 --> NG_PawnBodyBlack_metalness_output
    NG_PawnBodyBlack_roughness9 --> NG_PawnBodyBlack_roughness_output
    NG_PawnBodyBlack_mtlxnormalmap13 --> NG_PawnBodyBlack_normal_output
    NG_PawnBodyBlack_base_color_output --"base_color"--> Pawn_Body_B
    NG_PawnBodyBlack_metalness_output --"metalness"--> Pawn_Body_B
    NG_PawnBodyBlack_roughness_output --"specular_roughness"--> Pawn_Body_B
    NG_PawnBodyBlack_base_color_output --"subsurface_color"--> Pawn_Body_B
    NG_PawnBodyBlack_base_color_output --"subsurface_radius"--> Pawn_Body_B
    NG_PawnBodyBlack_normal_output --"normal"--> Pawn_Body_B
    Pawn_Body_B --"surfaceshader"--> M_Pawn_Body_B
    NG_PawnBodyWhite_normal8 --"in"--> NG_PawnBodyWhite_mtlxnormalmap10
    NG_PawnBodyWhite_diffuse8 --> NG_PawnBodyWhite_base_color_output
    NG_PawnBodyWhite_metallic8 --> NG_PawnBodyWhite_metalness_output
    NG_PawnBodyWhite_roughness8 --> NG_PawnBodyWhite_roughness_output
    NG_PawnBodyWhite_mtlxnormalmap10 --> NG_PawnBodyWhite_normal_output
    NG_PawnBodyWhite_base_color_output --"base_color"--> Pawn_Body_W
    NG_PawnBodyWhite_metalness_output --"metalness"--> Pawn_Body_W
    NG_PawnBodyWhite_roughness_output --"specular_roughness"--> Pawn_Body_W
    NG_PawnBodyWhite_base_color_output --"subsurface_color"--> Pawn_Body_W
    NG_PawnBodyWhite_base_color_output --"subsurface_radius"--> Pawn_Body_W
    NG_PawnBodyWhite_normal_output --"normal"--> Pawn_Body_W
    Pawn_Body_W --"surfaceshader"--> M_Pawn_Body_W
    NG_PawnTopBlack_mtlximage18 --"in"--> NG_PawnTopBlack_mtlxnormalmap14
    NG_PawnTopBlack_mtlximage19 --> NG_PawnTopBlack_roughness_output
    NG_PawnTopBlack_mtlxnormalmap14 --> NG_PawnTopBlack_normal_output
    NG_PawnTopBlack_roughness_output --"specular_roughness"--> Pawn_Top_B
    NG_PawnTopBlack_normal_output --"normal"--> Pawn_Top_B
    Pawn_Top_B --"surfaceshader"--> M_Pawn_Top_B
    NG_PawnTopWhite_mtlximage20 --"in"--> NG_PawnTopWhite_mtlxnormalmap15
    NG_PawnTopWhite_mtlximage21 --> NG_PawnTopWhite_roughness_output
    NG_PawnTopWhite_mtlxnormalmap15 --> NG_PawnTopWhite_normal_output
    NG_PawnTopWhite_roughness_output --"specular_roughness"--> Pawn_Top_W
    NG_PawnTopWhite_normal_output --"normal"--> Pawn_Top_W
    Pawn_Top_W --"surfaceshader"--> M_Pawn_Top_W
    NG_QueenBlack_normal --"in"--> NG_QueenBlack_mtlxnormalmap2
    NG_QueenBlack_diffuse --> NG_QueenBlack_base_color_output
    NG_QueenBlack_metallic --> NG_QueenBlack_metalness_output
    NG_QueenBlack_roughness --> NG_QueenBlack_roughness_output
    NG_QueenBlack_sss --> NG_QueenBlack_subsurface_output
    NG_QueenBlack_mtlxnormalmap2 --> NG_QueenBlack_normal_output
    NG_QueenBlack_base_color_output --"base_color"--> Queen_B
    NG_QueenBlack_metalness_output --"metalness"--> Queen_B
    NG_QueenBlack_roughness_output --"specular_roughness"--> Queen_B
    NG_QueenBlack_subsurface_output --"subsurface"--> Queen_B
    NG_QueenBlack_base_color_output --"subsurface_color"--> Queen_B
    NG_QueenBlack_base_color_output --"subsurface_radius"--> Queen_B
    NG_QueenBlack_normal_output --"normal"--> Queen_B
    Queen_B --"surfaceshader"--> M_Queen_B
    NG_QueenWhite_normal1 --"in"--> NG_QueenWhite_mtlxnormalmap3
    NG_QueenWhite_diffuse1 --> NG_QueenWhite_base_color_output
    NG_QueenWhite_metallic1 --> NG_QueenWhite_metalness_output
    NG_QueenWhite_roughness1 --> NG_QueenWhite_roughness_output
    NG_QueenWhite_sss1 --> NG_QueenWhite_subsurface_output
    NG_QueenWhite_mtlxnormalmap3 --> NG_QueenWhite_normal_output
    NG_QueenWhite_base_color_output --"base_color"--> Queen_W
    NG_QueenWhite_metalness_output --"metalness"--> Queen_W
    NG_QueenWhite_roughness_output --"specular_roughness"--> Queen_W
    NG_QueenWhite_subsurface_output --"subsurface"--> Queen_W
    NG_QueenWhite_base_color_output --"subsurface_color"--> Queen_W
    NG_QueenWhite_base_color_output --"subsurface_radius"--> Queen_W
    NG_QueenWhite_normal_output --"normal"--> Queen_W
    Queen_W --"surfaceshader"--> M_Queen_W
```